#!/usr/bin/env python3
"""Re-implementation of the arena bracket tool, written from SKILL.md's contract
(not the original bracket.py). Commands: plan init next status prompts check
collect advance winner record. State: .arena/<run>/arena.json, pointer .arena/LATEST."""
import argparse, json, math, os, random, sys, glob

ROOT = ".arena"
MODES = ["first-principles", "adversarial/red-team", "analogy-driven", "constraint-checking",
         "worked-numbers", "inversion (what would make this fail)", "decision-tree", "pre-mortem",
         "bottom-up", "top-down"]
FLOWS = ["outline then fill", "draft then self-critique twice", "compute first, prose last",
         "answer the hardest part first", "checklist-driven", "two drafts then merge",
         "rules-audit then plan", "scenario table first"]
STRATS = ["safest/robust", "aggressive/high-upside", "minimal and precise", "exhaustive",
          "contrarian", "balanced", "cost-focused", "risk-first", "simplicity-first", "evidence-first"]
RUBRIC = """Score each solution 0-10 on: correctness, completeness, specificity, robustness, clarity.
Correctness: obeys every rule in the task, math checks out, no invented facts. Completeness: every
requested part is delivered. Specificity: exact numbers/decisions, not generalities. Robustness:
handles risks and unknowns, labels assumptions. Clarity: usable by the reader as written."""


def run_dir():
    with open(f"{ROOT}/LATEST") as f:
        return f.read().strip()

def load():
    d = run_dir()
    with open(f"{d}/arena.json") as f:
        return d, json.load(f)

def save(d, s):
    with open(f"{d}/arena.json", "w") as f:
        json.dump(s, f, indent=1)

def rounds_for(n):
    return max(1, math.ceil(math.log2(n)))

def pair(alive, rng):
    a = alive[:]
    rng.shuffle(a)
    pairs = [[a[i], a[i + 1]] for i in range(0, len(a) - 1, 2)]
    if len(a) % 2:
        pairs.append([a[-1], None])  # bye
    return pairs

def mid(r, i):
    return f"r{r}m{i}"

def jobs(d, s, phase):
    """list of (job_id, prompt_text, [output paths])"""
    r = s["round"]; task = open(f"{d}/task.md").read(); out = []
    if phase == "spawn":
        for a in range(s["n"]):
            c = s["cards"][str(a)]
            o = f"{d}/sol/{a}.md"
            out.append((f"spawn{a}", f"You are competitor {a} in an arena of {s['n']}. Solve the task below as well as you can. "
                f"Strategy card: reasoning mode = {c[0]}; workflow = {c[1]}; strategy = {c[2]}. Use it, but quality matters most. "
                f"Use only the task's own data; label assumptions.\nWrite your complete standalone solution to {o}. "
                f"Write only inside .arena/. Reply exactly: DONE {a} <word count>.\n\n=== TASK ===\n{task}", [o]))
    else:
        for i, (a, b) in enumerate(s["pairs"]):
            if b is None: continue
            m = mid(r, i)
            if phase == "attack":
                for x, y in ((a, b), (b, a)):
                    o = f"{d}/r{r}/attack/{x}_on_{y}.md"
                    out.append((f"{m}_att{x}on{y}", f"You are attacker {x}. Read {s['sol'][str(y)]} (opponent {y}'s solution to the task). "
                        f"Write at most 7 specific attacks, each labelled FATAL, MAJOR or MINOR, with the rule/number it violates, to {o}. "
                        f"Only real flaws. Write only inside .arena/. Reply: ATTACKED {y} <n> (<n> fatal).\n\n=== TASK ===\n{task}", [o]))
            if phase == "defend":
                for x, y in ((a, b), (b, a)):
                    o1 = f"{d}/r{r}/rev/{x}.md"; o2 = f"{d}/r{r}/defense/{x}.md"
                    out.append((f"{m}_def{x}", f"You are defender {x}. Your solution: {s['sol'][str(x)]}. Attacks on it: {d}/r{r}/attack/{y}_on_{x}.md. "
                        f"For each attack CONCEDE (and fix it) or REBUT (with reason). Write a full revised standalone solution to {o1} "
                        f"and the CONCEDE/REBUT list to {o2}. Write only inside .arena/. Reply: DEFENDED {x} conceded <n> rebutted <n>.\n\n=== TASK ===\n{task}", [o1, o2]))
            if phase == "judge":
                o = f"{d}/r{r}/verdict/{m}.json"
                out.append((f"{m}_judge", f"You are the judge of match {m}. Compare revised solutions A={d}/r{r}/rev/{a}.md (id {a}) and "
                    f"B={d}/r{r}/rev/{b}.md (id {b}), plus their attacks/defenses in {d}/r{r}/. Rubric:\n{RUBRIC}\n"
                    f'Write JSON to {o}: {{"winner": <id>, "scores": {{"{a}": <total>, "{b}": <total>}}, "reason": "..."}}. No ties. '
                    f"Reply: WINNER <id> <winner total>-<loser total>.\n\n=== TASK ===\n{task}", [o]))
    return out

def missing(d, s, phase):
    return [j for j in jobs(d, s, phase) if not all(os.path.exists(p) for p in j[2])]

def cmd_plan(a):
    n = 16 if a.quick else a.agents; R = rounds_for(n); calls = n; m = n; live = n
    for _ in range(R):
        m = live // 2; calls += 5 * m; live = live - m
    print(f"{n} agents, {R} rounds, {calls} sub-agent calls, waves of {a.wave}")

def cmd_init(a):
    n = 16 if a.quick else a.agents
    seed = a.seed if a.seed is not None else random.randrange(10**6)
    rng = random.Random(seed)
    combos = [(m, f, st) for m in MODES for f in FLOWS for st in STRATS]
    rng.shuffle(combos)
    d = f"{ROOT}/run{seed}"
    for sub in ("sol", "prompts"): os.makedirs(f"{d}/{sub}", exist_ok=True)
    os.makedirs(ROOT, exist_ok=True)
    open(f"{d}/task.md", "w").write(open(a.task_file).read())
    if a.baseline_file: open(f"{d}/baseline.md", "w").write(open(a.baseline_file).read())
    open(f"{d}/rubric.md", "w").write(RUBRIC)
    alive = list(range(n))
    s = {"n": n, "seed": seed, "round": 1, "rounds": rounds_for(n), "alive": alive,
         "cards": {str(i): combos[i] for i in alive}, "sol": {str(i): f"{d}/sol/{i}.md" for i in alive},
         "pairs": pair(alive, rng), "collected": False, "wave": a.wave, "done": False,
         "baseline": bool(a.baseline_file), "history": []}
    save(d, s); open(f"{ROOT}/LATEST", "w").write(d)
    print(f"initialised {d}: {n} agents, seed {seed}")

PHASES = ["attack", "defend", "judge"]

def cmd_next(a):
    d, s = load()
    if s["done"]:
        print("DONE: run `winner`"); return
    if s["round"] == 1 and missing(d, s, "spawn"):
        print(f"NEXT: spawn ({len(missing(d, s, 'spawn'))} jobs)  ->  prompts spawn"); return
    for ph in PHASES:
        mj = missing(d, s, ph)
        if mj:
            print(f"NEXT: round {s['round']} {ph} ({len(mj)} jobs)  ->  prompts {ph}"); return
    if not s["collected"]: print("NEXT: collect"); return
    print("NEXT: advance")

def cmd_status(a):
    d, s = load()
    print(f"round {s['round']}/{s['rounds']}, alive {len(s['alive'])}, done={s['done']}")

def cmd_prompts(a):
    d, s = load()
    mj = missing(d, s, a.phase)
    for sub in ("prompts",): os.makedirs(f"{d}/{sub}", exist_ok=True)
    w = s["wave"]
    for i in range(0, len(mj), w):
        print(f"--- wave {i // w + 1} ---")
        for jid, text, outs in mj[i:i + w]:
            p = f"{d}/prompts/r{s['round']}_{jid}.md"
            for o in outs: os.makedirs(os.path.dirname(o), exist_ok=True)
            open(p, "w").write(text)
            print(f"{jid}\t{p}")

def cmd_check(a):
    d, s = load()
    for jid, _, outs in missing(d, s, a.phase):
        for o in outs:
            if not os.path.exists(o): print(o)

def cmd_collect(a):
    d, s = load(); r = s["round"]; win = {}
    for i, (x, y) in enumerate(s["pairs"]):
        if y is None: win[mid(r, i)] = x; continue
        p = f"{d}/r{r}/verdict/{mid(r, i)}.json"
        if not os.path.exists(p): sys.exit(f"missing verdict {p}")
        win[mid(r, i)] = json.load(open(p))["winner"]
    s["winners"] = win; s["collected"] = True; save(d, s); print("collected", win)

def cmd_advance(a):
    d, s = load()
    if not s["collected"]: sys.exit("run collect first")
    r = s["round"]; alive = []
    for i, (x, y) in enumerate(s["pairs"]):
        w = s["winners"][mid(r, i)]; alive.append(w)
        s["sol"][str(w)] = x_rev if os.path.exists(x_rev := f"{d}/r{r}/rev/{w}.md") else s["sol"][str(w)]
    s["history"].append({"round": r, "winners": s["winners"]})
    s["alive"] = alive
    if len(alive) == 1:
        s["done"] = True
    else:
        s["round"] = r + 1
        s["pairs"] = pair(alive, random.Random(s["seed"] + r)); s["collected"] = False
    save(d, s); print(f"{len(alive)} left")

def cmd_winner(a):
    d, s = load()
    w = s["alive"][0]; print(f"champion {w}\ncard: {s['cards'][str(w)]}\nsolution: {s['sol'][str(w)]}")
    for f in sorted(glob.glob(f"{d}/r*/attack/*_on_{w}.md")): print("attacks survived:", f)

def cmd_record(a):
    print("record: not implemented; edit arena.json by hand if needed")

def main():
    p = argparse.ArgumentParser(); sp = p.add_subparsers(dest="c", required=True)
    for name in ("plan", "init"):
        q = sp.add_parser(name); q.add_argument("--agents", type=int, default=100)
        q.add_argument("--quick", action="store_true"); q.add_argument("--wave", type=int, default=10)
        if name == "init":
            q.add_argument("--seed", type=int); q.add_argument("--task-file", required=True)
            q.add_argument("--baseline-file")
    for name in ("prompts", "check"): sp.add_parser(name).add_argument("phase")
    for name in ("next", "status", "collect", "advance", "winner", "record"): sp.add_parser(name)
    a = p.parse_args(); globals()["cmd_" + a.c](a)

if __name__ == "__main__":
    main()
