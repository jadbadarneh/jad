# Erie Capsim "Foundation": all 16 candidate strategies, what happened to each

Purpose: hand this file to Claude and ask it to pick the best strategy for team Erie. It describes each plan neutrally, what attackers said about it, what its defender fixed, and why it won or lost. The order of the list is the competitor number, NOT a ranking.

## How these plans were produced
- Sixteen sub-agents each got the same task (the full Capsim brief: starting position, rules, Practice and Competition schedule, deliverables A to G). Each got a different "strategy card" (reasoning style, workflow, attitude).
- They then ran a single-elimination bracket. In each match, both sides attacked the other's plan (up to 7 flaws each, labelled FATAL, MAJOR or MINOR), then each defender conceded or rebutted every attack and rewrote the plan, then a judge scored both revised plans 0-10 on correctness, completeness, specificity, robustness and clarity.
- **Caveats:** The judges are the same kind of model as the competitors. Nobody tested a plan in the real simulation. Every net income, share and cash figure is the plan author's own model, built on assumptions (no tax, SG&A or wage-raise data in the brief, and no data for High Tech material cost or new-product development time). Treat numbers as directional. The pattern of risk is more useful than any single figure.
- Files: `.arena/run7/r*/rev/<n>.md` (local to the arena session, git-ignored). The champion is `erie-capsim-strategy.md` and plan 15 is `plan-15-lifecycle-differentiator.md`, both in the repo.

## Bracket results (for reference)
| Round | Matches (winner first, score) |
|---|---|
| 1 | 7 over 13 (40-37); 1 over 2 (41-38); 9 over 11 (42-40); 12 over 0 (42-38); 14 over 10 (40-35); 5 over 8 (43-36); 15 over 6 (41-36); 3 over 4 (41-39) |
| 2 | 5 over 7 (42-36); 15 over 14 (41-36); 3 over 1 (42-39); 12 over 9 (40-37) |
| 3 | 5 over 15 (43-38); 3 over 12 (42-37) |
| 4 (final) | 3 over 5 (42-38) |

## Vocabulary used below
- **LT / HT:** Low Tech / High Tech segment. LT is bigger early (70% of demand, grows 10% a year); HT is 30% and grows 20% a year, so HT is about 46% of demand by R8.
- **Eat:** the one product every company starts with. It sits between the segments.
- **Reposition:** changing Pfmn/Size halves the product's age. The LT ideal drifts 0.5 a year and the HT ideal 0.7 a year, so products must be moved.
- **Worst-case cash test:** production is set from the best-case forecast, then December 31 cash is checked on a low forecast, so there is never a negative-cash "emergency loan".
- **Fine cut:** 2.5 units around a segment's center. Outside it, scores drop sharply.
- **CM:** contribution margin. The instructor slide says 30% or higher is the target.

---

## #0: Broad Cost Leader in Low Tech plus a lean High Tech entrant
**Plan.** Eat becomes a cost-trimmed LT product (5.3/14.7, MTBF 20,000), with automation raised later. One new HT product "Edge" has its line bought in R1 and launches in R2. The HT leg is not a cost play (top-of-range price, minimal selling cost). "Broad" means it competes in two segments.
**What happened.** Lost round 1 to #12 (38-42).
**Attacks on it.** The three old bond maturities ($867K in R2, $1,733K in R4) were missing from the cash math, and it told you to retire bonds already matured. CR2 cash was about $3.5M, not the stated $4.8M, and CR3 about $5.7M, not $7.0M. The CR1 net income did not match its own 35% tax assumption.
**Defense (conceded all seven).** Put all three maturities (R2, R4, R6) into every cash roll. Withdrew its "capacity cliff" idea (industry capacity R3 10,932 vs demand 10,440 is only 4.7% slack). Eat holds 5.3/14.7 through R3, then moves to 6.0/14.0 in R4 and 7.0/13.0 in R6. Price held at $34 in R1-R3. R1 current debt raised from $4.0M to $6.5M, so worst-case R1 cash goes from -$2.2M to about +$0.1M. One go/no-go rule: Edge's revision must be on or before Jul 1 of R2, and the slip scenario stays solvent (R2 cash about $4.3M).
**Why it lost.** Judge: #12 had a per-product promo/sales table for all rounds and a cash bridge that re-adds. #0's overview table was stale, CR4-CR8 cash was partly approximate, its 32-34% CM targets rest on HT material costs the brief doesn't give, and it needs Edge's revision date to land by Jan 1 of R2.
**Strengths.** Holding Eat at 5.3/14.7; a candid bound on how much price changes volume.

## #1: Differentiator with a gated High Tech product "E1" and a Low Tech-only fallback
**Plan.** Eat is a cheap LT product. A new HT product E1 launches early. A decision gate at the end of PR2 chooses between the HT plan and a pure-LT fallback. The plan calls itself a higher-variance bet.
**What happened.** Beat #2 in round 1 (41-38). Lost round 2 to #3 (39-42).
**Attacks, round 1 (by #2).** Strategy rests on assumed shares, not CSS logic; its own stress cases ($28.3M, $19.8M cumulative net income) fall below its LT-only fallback ($32.0M); it breaks its own "max 2 concurrent projects"; no cash math for R5-R7; it deliberately departs from the "produce from the best case" rule; about $301K of interest left out; the Eat reposition date came from an MTBF-21,000 book example although the plan sets 20,000.
**Defense.** Added a CSS build for E1 and a break-even (needs rival HT CSS of about 46 or less for a 28% share); gate G0 at the end of PR2; at most 2 concurrent projects; cash builds for R5-R8; R2 dividend cut to $0; current debt $4.0M.
**Attacks, round 2 (by #3).** FATAL: the plan hard-codes 60-day A/R from R3 but leaves the extra receivables ($6.5M in R3, $13-16M by R7-R8) out of its cash math. Fine cut was measured from the HT ideal instead of the center. Breaks the best-case-production rule and leans on an unverified $8.9M debt limit. Alternatives and CM figures had no math. It hedges between two strategies.
**Defense.** A/R 30 days in every round (60 only a funded option); E1 stays in the HT fine cut through R6; R1 current debt $5.9M everywhere; unit-economics builds reproduce R2 CM 31.7%, R3 30.9%, R4 about 27%; cumulative net income restated to $44.6M (from $47.4M) with a stress floor of about $17.0M.
**Why it lost.** Judge: #3 followed the best-case-production rule and ran one worst-case formula; #1 knowingly deviates, its alternatives rest on a crude net income model it admits it can't reproduce, its gates partly hedge the "one strategy" requirement, margin falls to 25-27% from R4, and HT material cost is extrapolated well past the data.
**Strengths.** Richer HT geometry, CSS and R&D schedules than most.

## #2: Broad Differentiator, High Tech first
**Plan.** Eat stays a high-margin LT cash product. New HT products launch first and alone and are revised every year to stay HT. Capacity is bought a year ahead, the second shift is used as cheap capacity, and prices sit at the top of range. Edge launches in R2, with Echo later.
**What happened.** Lost round 1 to #1 (38-41).
**Attacks (by #1).** R2 Edge volume of 435K exceeds the half-year ceiling of 340K; R2-R4 cash didn't sum (R3 5.9M vs 6.3M stated, R4 8.3M vs 9.1M); the R7-R8 "roll down" kept Edge at $45 although LT tops at $35; alternative net income figures were asserted; Eat at $35 contradicted its own price math; a second Edge R&D project started while the first was unfinished.
**Defense.** Edge R2 capped at 340K; every round re-summed (ending cash R2 $3.8M, R3 $5.6M, R4 $7.6M, R5 $14.2M, R6 $7.2M, R7 $6.8M, R8 about $5M); roll-down dropped (Edge and Echo revised every year through R8); R3 dividend cut to $0. Alternatives now derived: cumulative net income $63.7M for the plan vs $19.9M for Niche Cost Leader, $42.8M for HT-only and -$64.2M for Broad Cost Leader; a stress test (LT share 12%, HT units -20%) still leaves about $42M. Added a 12% LT-share floor rule for stepping price down.
**Why it lost.** Judge: #2 is cleaner and derives alternatives from one model, but its Edge line is thin, Eat at $35 is unstressed with a flat 15% LT share, the worst-case inventory knowingly breaches 1/6, and it is thinner on HT CSS logic than #1.

## #3: Niche Cost Leader in Low Tech ("LT Capacity Wall") — CHAMPION
**Plan.** Three LT products (Eat, Ease, Edge) on separately financed lines, all at the cheap trailing edge of LT, MTBF 20,000, price held at the LT ceiling ($35). Eat is repositioned to 5.3/14.7 in R1 (revision around Nov 9, material about $12.00). Ease launches about Apr 1 of R2 and Edge about Apr 1 of R3. Lines are bought a year ahead, but a line is only expanded if next year's production would exceed 1.85x its first-shift capacity (Eat is never expanded). No stock issue; bonds plus current debt; cash goes back out from R4 (debt payoff, dividends up to EPS, retirement). High Tech only via a four-gate Stage 2 product "Echo" (spec 10.5/9.5, line bought in R4, revision about Apr 1 of R5).
**Numbers (its own model).** Units 1,175 in R1 to about 4,000 in R8; contribution margin about 34% in R3, 28% in R5, 20% in R8; net income about $4.8M (R2), $6.5M (R3), $9.2M (R5), $8.1M (R8); EPS about $4.05 in R8, about $4.95 with Echo; total share 16-23% (16.7% is parity), 19.9% in R8 or 27.6% with Echo.
**What happened.** Beat #4 (41-39), #1 (42-39), #12 (42-37) and #5 in the final (42-38).
**Attacks it survived.** Round 1 (by #4): seven attacks, none fatal (details not kept in my notes). Round 2 (by #1): one FATAL, that its worst-case cash didn't use one consistent formula; the others were too few alternatives costed, the Edge-line gate, awareness, idle cash, A/R terms and unsourced numbers. Round 3 (by #12): its labor cost didn't follow its own second-shift mix (so CM was too high by 3-7 points from R5), capacity increments, no High Tech option costed, HR left untested, a PR2 test that contaminated the share read, and idle cash. Round 4 (by #5): $13.7M of capacity increments its own 1.85x rule didn't allow, the seller's-market finding never used, a base plan that leaves total share near parity, and a worst-case cash test tuned to land within a few $K of the floor.
**Defense highlights.** Single labor formula `8.96 x (1 + 0.5 x second-shift share)` checked against the R0 screen (it reproduces $10.65 vs $10.60); capacity rule restated per line, not pooled; per-product repositioning schedule keeping every product within about 2.0 of the LT center through R8; Branch S (seller's-market price ladder) priced but kept out of the base plan; accessibility now decays by one third a year (R1 about 49%, not 62%); Tier-2 worst-case test and standing current-debt buffer; Echo's launch-year volume cut from 800k to 525k.
**Why it won the final.** Judge: full 8-round plan, per-line capacity rule, two-tier worst-case cash tests that include bond maturities, a priced seller's-market branch, a corrected accessibility error, and honesty that the base plan is not the whole-market share leader.
**Weaknesses it admits.** Not the share leader (16-23%); CM falls below 30% from R5 because the drift forces repositioning up the material-cost curve; below the average rival in R2; base plan assumes rivals don't cut LT prices much; MTBF trim is break-even, not a margin lever; cash figures are modelled, not proforma output.

## #4: Broad Differentiator, High Tech weighted, "Cow funds Rocket"
**Plan.** Eat is an LT cash cow (first-shift CM about $12.8 at $34, about $14.8M contribution on about $46M revenue, about 32%). That cash funds a High Tech "Elite" and a later "Epic". Elite revisions follow a rule: each year-end HT center plus 2.0 per axis (8.7/11.3, 9.4/10.6, 10.1/9.9, 10.8/9.2, 11.5/8.5, 12.2/7.8).
**What happened.** Lost round 1 to #3 (39-41).
**Defense (conceded all seven).** Added late-game HT capacity (500 in R6, 400 in R7, gated; 2,700 first-shift HT capacity in R8); R1 Elite line cut to 460 with $3.5M current debt, base Dec 31 cash +$4.7M and worst case +$1.0M; Eat repriced with interpolated price scores (contribution $14.8M at $34, $12.5M at $32, $8.6M at $29), so Eat is held at $34 in R2-R4 and $33 in R5-R8; R2-R8 cash table rebuilt (base cash positive; downside case bottoms at $2.3M). Cumulative contribution about $233M over R2-R8, CM about 28-29% after repricing; leverage after R1 about 1.8.
**Why it lost.** The match was close (39-41). I don't have the judge's written reasons for this match, only the score.

## #5: Broad Differentiator (runner-up)
**Plan.** Eat is a cost-trimmed LT cash line ($34 flat, 5.4/14.6 or the cheaper 5.9/14.1 fallback; material $15.97 to about $12.2-12.5). A new HT product "Edge" starts Jan 1 of R1 and sells from Jan 1 of R2 at $39 rising to $44, MTBF 23,000, $1.5M promo and a $3.0M sales budget, and is repositioned about 0.7 a year (8.5/11.5 in R2). Edge's line is bought in R1 and grows about 150-260 a year; Eat adds 90 in R2. Funded by bonds ($4.2M in R2, $3.5M in R3, $2.0M in R4, $2.6M in R6) and $3.5-4.5M of current debt; no stock, no dividends until R7.
**Numbers.** Cumulative net income $41.2M vs $38.3M for the Niche Cost Leader fallback (+$2.9M, +8%), only if Edge reaches about 15.2% of High Tech; go/no-go gate set at 16%. CM above 30% only in R2-R4, falling to 17.6% by R8. Worst-case cash at least $1.5M every round (the lowest is R6 at $1,910K).
**What happened.** Beat #8 (43-36), #7 (42-36) and #15 (43-38). Lost the final to #3 (38-42).
**Attacks.** Pooled-accessibility claim retracted (Eat and Edge are in different segments); cash floor missed in R2, R3, R8; 17% Edge share is an unsupported placeholder; Edge's launch revision date must be exactly Jan 1 of R2 with no slack; the "seller's market" trigger tested totals instead of per segment; the "one strategy" is really a conditional gate; CM target lowered to fit the model; Eat held at 17% share and $34 for 8 years while predicting rival price cuts.
**Defense.** Rebuilt cash tables (worst case at least $1.99M); new Edge-launch stress (Edge 15% below plan still $1.58M); gate raised to 16%; Eat held at $34 with $35 as a PR2 test; per-segment seller's-market trigger.
**Why it lost.** Judge: lead over the fallback is thin and depends on an unsupported 17% Edge share; the gate reads practice rounds that reset before competition; no slack on the Jan 1 Edge date; CM falls to 17.6%; the $1.5M cash floor is its own assumption.

## #6: Broad Differentiator with High Tech "Edge" then "Elan"
**Plan.** Edge targets 8.1/11.9 with launch about April 19 of the following year; the Edge line (300K) is bought in R1 only if the R&D screen shows a revision date no later than Jul 1 of R2. Edge's first reposition project is in R3. A third product "Elan" is gated on four conditions (first-shift output, ending inventory or stock-outs, uncovered HT demand, worst-case cash). Eat's price comes from a sweep on the Marketing screen starting at $33; Eat's project moved to R4 so it doesn't overlap Elan's.
**What happened.** Lost round 1 to #15 (36-41).
**Defense.** R1 worst-case cash is about -$4.2M without borrowing; a $5.5M current-debt draw plus the smaller Edge line brings it to about $1.26M (base about $4.5M). R1 CM target cut to 18-22% with a hard floor of 17%; R1 net loss about $1.2M vs about +$2.1M at defaults. R3 cash made one consistent figure (-$3.7M before financing, $3.9M after).
**Why it lost.** Judge: #6 is denser and clearer and it alone caught the "unfinished project" rule, but its R1 plan relies on $5.5M of current debt against an unverified limit, and its worst-case checks stop after R3. #15 had worst-case cash tables for every investment round R1-R8.

## #7: Capacity-led Niche Cost Leader in Low Tech, in two stages
**Plan.** Stage 1 (R1-R2, meant to be robust under any rival scenario): move Eat onto the drifting LT corridor in R1, keep it cheap, young (age about 2.2-3.6) and always in stock, buy about +300 capacity a year ahead. Stage 2 (R3+): grow LT share by adding a second LT product (Branch P, the default) or a bigger 3,750-unit ladder (Branch S, gated).
**What happened.** Beat #13 in round 1 (40-37). Lost round 2 to #5 (36-42).
**Attacks (by #5).** $48M of capex sized on a 35% LT share that CSS math doesn't support; overcapacity gate G1 could never fail; price defence tested only one rival cutting; liquidity relied on current debt for capex; HT rejection had no shown math; total share ends at 18.7%; the 20% worst case marked "n.a." in several rounds.
**Defense.** LT share derived from CSS ratios (about 19% R1, 22% R2-R3, 16.7% against repositioning rivals); Branch P as default; G1 rewritten so it can fail; price defence re-run for five cutters; tier-2 worst-case cash every round; dividends conditional, stock issue named as the capex fallback; HT rows withdrawn and replaced with a per-line comparison. Branch P's cash tables were not fully re-run, so its numbers are approximate.
**Why it lost.** Judge: weaker justification; alternatives unsupported; relies on large current debt ($12-15M) to fund capex, which the brief reserves for working capital; "cost leader" redefined as pricing at the ceiling; bloated with revision notes.

## #8: Differentiator with Product Lifecycle Focus (scenario S3)
**Plan.** Eat is an LT cash product at $35 and about $12 material. New HT products launch every second year at the HT ideal, are repositioned +0.7 every year, and eventually glide into LT. Scenario S3 targets about 2,550 units in R4 (Eat 1,400, Edge 500, E3 650) at about 32% CM, about $140M revenue by R8.
**What happened.** Lost round 1 to #5 (36-43).
**Defense (conceded all seven).** Edge repositioned +0.7 every year, year-end distance 1.98, under the fine cut; "simultaneous R&D projects" assumed company-wide; R5 capex cut from $13.4M to $7.2M; Eat automation upgrade moved to R6; R1 stock issue and R5 bonds removed; current debt resized R2 $2.7M, R3 $2.3M, R4 $2.6M, R5 $0; worst-case cash about $0.5-0.8M. It admits the S1 (LT only, two lines, automation 5) R4 net income ($11.9M) is slightly above S3's ($11.1M) and argues for S3 on R8 revenue and unserved HT demand.
**Why it lost.** Judge: net income figures come from a fit of two unknowns to one data point; R5-R8 rows are thin and optimistic (net income about $21-23M); the $35 price ignores the range-edge price penalty; no cash table for R6-R8; accepts inventory above the 60-day limit in the worst case.

## #9: Broad Differentiator, Edge launched at the middle of the HT path
**Plan.** Edge launches at the midpoint of the HT ideal's path (8.4/11.6 in R2) and moves one 0.7 step every Jan 1. Eat moves to 5.9/14.1 in R1 (not 5.4/14.6) because the fine cut is around the segment center, saving $404K R&D. Prices at the top of the range give CM about 30.7-30.8% in R2-R3, then falling (30.3 / 29.4 / 27.7 / 26.2 / 24.5 / 22.8 / 20.5% over R2-R8 under conservative HT material costs; about 33% in R8 if HT material saturates near $17.3). Small dividend path capped at EPS.
**What happened.** Beat #11 in round 1 (42-40). Lost round 2 to #12 (37-40).
**Attacks (round 2, by #12).** Labor cost claim; Edge age; no cash math for R5-R8; A/R; Edge R2 volume vs the 1/12 monthly cap; net income didn't tie; Edge and Elan stacked volumes.
**Defense.** Labor formula `8.96 x (1 + 0.5 x 487/1,287) = $10.65` shows the screen's $10.60 is a blended figure; Edge steady-state age 1.5 at year boundaries; R5 capex cut from $10.8M to $8.1M; R2-R5 financing rebuilt so every worst case is at least $500K; Edge and Elan share volume instead of stacking.
**Why it lost.** Judge: #12's cash buffers are bigger. #9's worst-case margins are thin ($518-601K vs a $500K floor), it pays dividends while drawing current debt, and its R6-R8 math is only summarized. #9 is rigorous on labor, age algebra and A/R.

## #10: Differentiator with Product Lifecycle Focus, Edge and Echo
**Plan.** Material cost for HT extrapolated from the book (Edge about $19.0, Echo about $21.2-21.8 at MTBF 22,000). Edge CM at $38 about 26%, Echo about 23%. Case for HT rests on volume in a segment growing 20% a year, not on margin. Ezra dropped from the base plan (CM about 14%). The model gives cumulative net income of $28.0M for the base plan vs $22.1M LT-only; R8 reconciles at 3,000K units and $104.4M revenue.
**What happened.** Lost round 1 to #14 (35-40).
**Defense.** R1 worst-case Dec cash -$1,134K before borrowing; a $2.5M current-debt draw gives +$1,366K; R1 forecast 1,120 (the benchmark); price ladder stops at $35; kill criterion on Edge's material cost.
**Why it lost.** Judge: by its own admission the plan is economically weak (CM falls to about 15%, profit about $4M on $104M revenue, the cost-leader alternative beats it on CM); uses the full R1 investment cap with a dilutive stock issue; thin cap margins in R2-R3; thinner R4-R8. Strengths: a good PR1 price test ladder and a clear kill criterion.

## #11: Broad Differentiator, High Tech-led, Low Tech-funded
**Plan.** An HT product "Edge" at about 7.4/12.6 launches in R2 and carries the plan, funded by the Eat LT cash line. Assumes a very high HT share (45-60%) because rivals are slow. Eat repositions in R4 (6.1/13.9), R6 (6.8/13.2) and R8 (7.5/12.5).
**What happened.** Lost round 1 to #9 (40-42).
**Defense (conceded six).** Edge's R2 spec set so there is about a 3.2-month buffer on the revision date; stock-price floor $7; R2 capex cut from $9,060K to $6,000K (worst-case R2 cash $1.3M); the missed $867K bond maturity added; R3 working-capital growth $4.5M (worst-case R3 cash $1.1M); Edge base price $40; Edge R2 CM cut from $11.6M to $9.4M.
**Why it lost.** Judge: #9 is more rule-faithful and better stress-tested. #11 covers all eight rounds with a rules audit and a Plan B, but its CM is only 17-20%, its 45-60% HT share depends on slow rivals, and its Edge timing and R2 financing rest on unverified assumptions.

## #12: Broad Differentiator, High Tech-led (staged)
**Plan.** Eat is the LT cost anchor; Edge launches on an assumed analogue date (Apr 19), with a slip table (Apr, Jul, Oct, one-year slip). HT material is run two ways (Case S: +$1.6 per Pfmn point, CM falls to about 19% by CR8; Case P: flat). Financing: bonds $2,480K plus about $1.9M current debt in CR1, no stock; payouts only from CR7, and none while a current-debt buffer is outstanding; explicit end-game cash order (dividends up to EPS, stock retirement at the 5% cap, bond retirement if allowed).
**Numbers.** Cumulative EBIT R1-R8: $94.7M (Case S), $157.0M (Case P), $55.8M contested, against $38.7M for an Eat-only alternative. In round 3 it admitted a real automation-5 cost-leader alternative beats the HT build unless HT volume reaches about 70% of target; at 60% it loses by about $5.6M after tax. So the strategy became a staged option gated at 70% and 40% of target HT volume.
**What happened.** Beat #0 (42-38) and #9 (40-37). Lost the semifinal to #3 (37-42).
**Attacks (round 3, by #3).** CR1 forecast ignored its own promo response (stock-out risk); interest rates held fixed while leverage rises to about 2.3; alternatives weak (Alt 1 is just the Eat slice); interest total inconsistent ($14.1M vs $16.26M); borrows while paying nothing for six rounds; precise figures rest on an uncalibrated model (it gives CSS 26/21 vs the real 18/16); Eat ends CR8 at 2.69 from the LT center, outside the fine cut.
**Known gap after its last revision.** The CR2-CR8 bridges still use a $42 HT price while the revised text says the CR2 launch price is $40 until PR2.
**Why it lost.** Judge: #3 was more consistent (one sourced labor formula checked against R0, worst-case cash every round, gates on measured values, HR tested). #12 depends on an unsupported HT launch date, extrapolated HT material cost and assumed HT shares, admits the model is off by about 30%, and holds borrowed cash while paying out nothing for six rounds. Strength: alternatives with real numbers.

## #13: Broad Differentiator, High Tech-led with Eat as LT cost anchor
**Plan.** HT products "Edge" and "Elan"; expansion is capacity-gated. R1: bonds $2.48M plus $5.0M current debt, a smaller 300K Edge line ($5.4M), no stock (R1 leverage about 2.1 vs about 1.7 with a stock issue). Edge sells at most 300K in R2 (250K planned); R2 net income about $2.9M, cash about $6.8M. Eat held at $34 every round (CM about 31.8% in R2, 30.1% in R3). HT price stays $40; PR3 tests $38 against $40.
**What happened.** Lost round 1 to #7 (37-40).
**Attacks (by #7).** Two FATAL: the R3 capex ($12.6M for Elan) exceeded the estimated max-investment cap, and Edge's R2 volume exceeded the launch-year output limit. The defense cut R3 capex to Elan 300 at $5.4M (inside a cap of about $6.4M with stock valued at $8) and checked R4 capex against about $7.0-7.4M.
**Why it lost.** The judge gave only the score (40-37 for #7).

## #14: "Anchor + Flagship" (Broad Differentiator: LT anchor plus HT flagships)
**Plan.** Eat is the LT anchor: 5.3/14.7 in R1, a micro-move in R3, then 6.4/13.6 in R4 and 7.3/12.7 in R6 so it stays inside the fine cut. Price $34 in R1, $33 in R2, $32 from R3. HT flagships Edge and E3; HT capacity is bought every year to R7 so first-shift HT capacity reaches 2,000 by R8. R2 capex 9,000 (Edge +250, Eat +250) inside the estimated cap; R1 current debt $2.5M. CR5-CR8 prices above range only if a seller's market is confirmed.
**Numbers.** In its own model R3 CM is $22.2M for the chosen plan, $21.7M for Alt 1 (a second LT line) if LT isn't crowded and $19.4M if it is, so R3 CM doesn't decide the choice; the choice rests on HT growth, the HT price ceiling and single-segment risk. Worst-case cash floor of $2M every round.
**What happened.** Beat #10 (40-35). Lost round 2 to #15 (36-41).
**Attacks (round 2, by #15).** CR8 books 3,060 HT units vs a ceiling of 2,900; E3's CR4 launch books 780 units although its revision isn't before Jan 1, 2030 (the "Apr 19" figure is the book's Eat-to-HT time, reused for a new product); the chosen-vs-Alt1 CM comparison used inconsistent bases; worst-case cash about 0 in CR4-CR6; the LT price rests on an illustration with rival CSS fixed at 62; "$12 LT material lasts four years" is really about 2.5 years; HR left at defaults.
**Defense.** Capacity rule changed to keep each product's available units at or below 85% of its two-shift ceiling; Edge CR2 cut from 450 to 380 units and E3 CR4 from 780 to 420; strategy comparison redone on one basis (including second-shift labor); late-game Eat material raised to about $17.1; HR rule E10 tests one lever per practice round. R4-R8 cash is estimated by delta only (about ±$2M).
**Why it lost.** Judge: #15 had full cash math every round R1-R8; #14 is candid and withdrew its CSS illustration, but its R4-R8 cash is only delta-estimated, it leans on an invented "crowded" case, its worst-case floor uses only -10% volume, and it holds idle borrowed cash with no dividend until R6.

## #15: Differentiator with Product Lifecycle Focus
(Full detail in `plan-15-lifecycle-differentiator.md`.)
**Plan.** Eat becomes a cheap LT cash cow in R1 (5.3/14.7, MTBF 20,000, material about $12.00, saving about $3.4M a year at Eat's volume), priced $32 in R1 and $30 after. A new young HT product "Edge" starts Jan 1 of R1 (target 8.1/11.9, MTBF 23,000, automation 3) with its 330K line bought in R1, launching about Jul 1 of R2, priced $42 rising to $44, repositioned each year. Edge capacity is bought each year but, from R4, capped by Edge's measured HT share. Eat is repositioned twice (R4 to 5.9/14.1, R6 to 6.9/13.1). Financing: bonds, 100K-share stock tranches in R1-R3, current debt up to $11M in R4-R6; no dividend in R1-R4, then $2.5M, $5.0M, $4.5M, $4.5M.
**Numbers.** CM 27% (R2-R3), 25% (R4), 23% (R5), 21% (R6), 17% (R7), 15% (R8). Worst-case cash at least $0.7M every round (R3 tightest). Net income about $6.5M in R3 rising to about $9.7M in R8.
**What happened.** Beat #6 (41-36) and #14 (41-36). Lost the semifinal to #5 (38-43).
**Attacks (round 3, by #5; 1 FATAL).** The R3 current-debt limit was overstated ($9.5M vs about $8.4M from the plan's own R2 sales); the Edge share claim fails under a common CSS-scale error; new-bond interest left out; idle cash while paying 8.6% and 10% interest; R1 dividend cut and stock-price claim unsupported; Edge's position lags the drifting ideal; arithmetic errors.
**Defense.** R3 debt cut to $7.5M with a second stock tranche; the missed 2030 and 2032 maturities added (forcing a redesign: debt $11.0M in R4-R6, dividends from R5); R4 bond dropped; stock-price recovery claim removed; Edge position trade-off priced.
**Why it lost.** Judge: it over-finances because of an invented -18% revenue shock, leaving $25-28M of idle cash next to 8.6% debt; #5's cash table, bond and max-investment checks and $1.5M worst-case floor agreed with its plan table.

---

## Cross-cutting patterns (useful when picking)
1. **Plans split into two families.** Low Tech first (#3, #7, #0 and #12's fallback) and High Tech-led or hybrid (the other 12). The Low Tech plans have better margins early and survive cash tests more easily. The High Tech plans chase 20% growth and a higher share but rest on unmeasured things: a new product's development time and launch date, HT material cost beyond 7.4/12.6, and Edge's share.
2. **Missing facts that drive the High Tech plans.** The brief gives no new-product R&D time, no HT material cost at the positions needed, and no HT price/share response. Every HT plan's profit depends on them. Practice rounds PR1-PR5 can measure these (the simulation resets afterwards), so a sensible approach is to choose a plan that is robust before measuring and has a clear gate after.
3. **Recurring errors attackers found.** Forgotten bond maturities (R2 $867K, R4 $1,733K, R6 $2,600K); the fine cut measured from the ideal instead of the segment center; 60-day A/R without its cash cost; new-product launch-year volume above the 1/12-per-month ramp; current debt used for capex while the brief says it is for working capital; margins not reaching the instructor's 30% after about R4; and numbers from models calibrated to one data point.
4. **Margin.** No plan holds 30% CM beyond about R4. The reason is that repositioning toward the leading edge raises material cost while the price is capped.
5. **Share vs profit.** The Low Tech wall (#3) leads in profit, EPS and units from R3 but not in total share; the High Tech plans (and #3's gated Echo) are the route to a higher total share.

## Suggested question for the picking Claude
"Given the brief (not in this file) and the 16 plans above, which plan would you run for Erie, and what would you change? Weigh rank-based vs Balanced Scorecard grading, cash-safety in R1-R3, how much each plan depends on unmeasured facts, and what PR1-PR5 can measure."
