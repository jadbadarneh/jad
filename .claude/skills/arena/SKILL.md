---
name: arena
description: >-
  Make 100 versions of Claude fight to the death over one task. Spins up N
  sub-agents (default 100, --quick for 16), gives every one the exact same
  task plus a different strategy card (reasoning mode, workflow, strategy),
  then runs a single-elimination bracket: they attack each other's solutions,
  defend and revise, and a judge scores every match on a written rubric until
  one solution survives. Use when the user is not satisfied with an answer,
  calls it a bad answer, says try again or do better, says "arena", or asks
  to make them compete.
argument-hint: "[--agents N | --quick] [--seed S] <task>"
---

# arena

For when Claude keeps giving a bad answer. Instead of asking again and again, this runs a tournament:
N sub-agents get the exact same task, each attacks it with a different reasoning mode, workflow and
strategy, and then they attack each other in a bracket until one solution is left. You are the
orchestrator. You never compete and you never judge.

What the user typed after `/arena`: `$ARGUMENTS`

If that is blank, or still reads like a placeholder, nothing was passed: take the task from the
conversation.

## The tool

Every piece of bookkeeping goes through `bracket.py` in this skill's folder:

```bash
python3 "${CLAUDE_SKILL_DIR}/bracket.py" <command>
```

Below, `ARENA` means exactly that command. If the path looks unexpanded, use the "Base directory for
this skill" that Claude Code printed at the top of this skill. The state lives in
`.arena/<run>/arena.json` in the current directory, and every command after `init` finds it through
`.arena/LATEST`.

## Step 1: size it, and get a yes if nobody asked for it

Read the flags out of the request. Everything that is not a flag is the task.

| flag | meaning |
| --- | --- |
| `--agents N` | N competitors. Default 100. |
| `--quick` | 16 competitors. The everyday setting. |
| `--seed S` | Fixes the cards and the pairings. Default: random, and recorded. |
| `--wave W` | Sub-agents per wave. Default 10. Only raise it if the user raised Claude Code's limit. |

No task text at all means: the task is the user's most recent request in this conversation, and your
last answer to it is the baseline to beat.

Run `ARENA plan --agents N` (or `--quick`). It prints the rounds, the sub-agent calls and the waves.

- **The user asked for the arena** (typed `/arena`, said "arena", or asked to make them compete):
  tell them in one line how big it is, for example "100 agents, 7 rounds, 595 sub-agent calls", and
  start.
- **This skill fired because the user is unhappy** ("that's wrong", "try again", "bad answer") and
  never mentioned the arena: ask once before spending anything. Offer three options: the full arena
  (100 agents, 595 sub-agent calls), `--quick` (16 agents, 91 calls), or an ordinary retry. Wait for
  the answer.

Sub-agents write their work into `.arena/` in the current directory. In the default permission mode
that is one approval per file, which is hundreds on a big run. Before the spawn phase, suggest
accept-edits mode (Shift+Tab) for the run. Do not change the user's settings yourself.

## Step 2: write the task file

This is the step that decides the result. **Sub-agents cannot see this conversation.** Every
competitor, attacker and judge knows only what is in the task file, so write `.arena/task.md` to stand
on its own:

- The request, in the user's own words where you can.
- Every requirement and constraint the user stated anywhere in the conversation: audience, length,
  format, tone, stack, deadline, what must not change.
- The context a stranger would need: absolute paths of the files that matter, pasted data, what the
  product is, the conventions in the codebase.
- What "done" looks like, if the user said.
- If there is an answer to beat: what the user disliked about it, in their words.

Do not add requirements the user never gave. Do not write your own view of the right answer into it:
that pushes 100 agents the same way, which is the opposite of the point.

If there is an earlier answer the user was not satisfied with, write it word for word to
`.arena/baseline.md`.

## Step 3: init

```bash
ARENA init --agents N --seed S --task-file .arena/task.md --baseline-file .arena/baseline.md
```

Leave out `--baseline-file` when there is nothing to beat, and `--seed` to get a random one. `init`
copies the task into the run folder, deals every competitor a different strategy card with no
repeats, pairs round 1, and writes `arena.json`.

## Step 4: the loop

Always drive it with `ARENA next`. It reads the state on disk and tells you the next step and the
exact command.

Every phase that runs sub-agents works the same way:

1. `ARENA prompts <phase>` writes one brief per job and lists the jobs still to run, in waves.
2. Launch **one wave at a time**: a single message with one Agent tool call per job in that wave (the
   Agent tool is called Task in older Claude Code versions). Each call is:
   - `subagent_type`: `general-purpose`
   - `description`: `arena <job id>`
   - `prompt`: `Read <prompt path> and follow it exactly. It is your whole brief.`
   - `run_in_background`: false, where the tool has that option, so the wave comes back together.

   Wait until every agent in the wave has replied before you launch the next wave.
3. After the last wave, run `ARENA next`. If an output is missing it sends you back to the same
   phase, and `prompts` then lists only the missing jobs. Re-run those once. If a job fails twice,
   write the single line `NO OUTPUT` into each of its output files (`ARENA check <phase>` lists
   them) and move on. A missing attack counts as no attacks. A missing solution loses its match. A
   judge that fails twice gets a third, fresh run: never decide a match yourself.

The order `next` takes you through:

- **spawn**, once: every competitor writes its own solution to the task.
- then every round: **attack** (two per match) → **defend** (two per match) → **judge** (one per
  match) → `ARENA collect` → `ARENA advance`.
- **final**, once, only when there is a baseline: a judge compares the champion with the answer the
  user rejected, blind to which is which. Then `ARENA collect`.
- `next` prints DONE: go to step 5.

After each `advance`, give the user one line, such as "Round 2 done: 25 of 100 left." Nothing more.
Never paste pairings, attacks, verdicts or solutions into the chat.

Why waves: Claude Code runs at most 10 tool calls at once by default (the
`CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY` setting). So a 100-agent spawn is 10 waves of 10, and a
100-agent arena is 70 waves in total, 71 with the final check.

## Step 5: the result

Run `ARENA winner`, then read the champion's solution file at the path it prints. That is the only
solution file you read in the whole run. Give the user:

1. **The winning solution**, in full.
2. **Why it won**: the attacks it survived, from `winner`, as a short list. Its card on one line
   (reasoning mode + workflow + strategy).
3. **Rounds**: for example "7 rounds, 100 agents in, 1 left."
4. **Against the answer you rejected**, if there was one: the final check's scores, honestly. If the
   old answer scored higher, say so plainly and show both.
5. Where the full record lives: the run folder.

If the solution changes files in the user's project, do not apply it. Ask: apply it, or change it?

## Rules for the orchestrator

- You run the tournament. You do not compete, attack or judge, and you never pick a winner.
  `collect` records what the judges decided. `record` is only for fixing bookkeeping when the user
  asks you to.
- Every sub-agent gets the task through its brief, which `prompts` builds from the one task file,
  byte for byte the same for everyone. Never paraphrase the task for one agent or add a hint to one
  agent's call.
- Do not read solutions, attacks or verdicts during the run. There are hundreds of them. The state
  is on disk, and `next`, `status` and `pairings` are all you need.
- If your context gets compacted mid-run, nothing is lost. Run `ARENA status`, then `ARENA next`,
  and carry on.
- Run every `ARENA` command from the directory you ran `init` in. That is where `.arena/LATEST`
  lives.
- Sub-agents only write inside `.arena/`. If one wrote anywhere else, tell the user.
- If the user says stop, stop. `ARENA status` shows where it got to, and `ARENA next` resumes it
  later.

## The prompt templates

`bracket.py` fills these in (the `{{placeholders}}`) and writes one brief per job, so what you see
here is exactly what every sub-agent is told. Never edit a brief for a single agent.

### Competitor, in the spawn phase
(template:competitor — "You are competitor {{agent}} in an arena of {{n}}…": gets the task, a strategy card (reasoning mode / workflow / strategy), writes its solution to {{out}}, replies `DONE {{agent}} <words>`)

### Attacker, in every round
(template:attacker — reads the opponent's solution, writes at most 7 specific attacks labelled FATAL/MAJOR/MINOR to {{out}}, replies `ATTACKED {{target}} <n> (<n> fatal)`)

### Defender, in every round
(template:defender — CONCEDE or REBUT each attack, writes a revised standalone solution and a defense file, replies `DEFENDED {{agent}} conceded <n> rebutted <n>`)

### Judge, one per match
(template:judge — scores both revised solutions 0–10 on correctness, completeness, specificity, robustness, clarity against `rubric.md`, writes a JSON verdict, replies `WINNER <id> <winner total>-<loser total>`)

### Final check, only when there is an answer to beat
(template:final — blind X/Y comparison of the champion against the rejected baseline, writes a JSON verdict, replies `FINAL <X or Y> <X total>-<Y total>`)
