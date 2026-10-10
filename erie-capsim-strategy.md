# Team Erie, Capsim Foundation: "LT Capacity Wall" (Niche Cost Leader, multi-product Low Tech) - REVISION 4

Labels: **ASSUMPTION** = my inference, not in the brief. **VERIFY** = check on a screen or spreadsheet before trusting. Units and capacity in thousands (k); dollars in $K unless "$M".

**What changed vs revision 3 (after the round-4 attack):**
1. **Accessibility now uses the brief's decay rule** (start = last year x 2/3, then add the budget effect). R1 accessibility is ~49%, not 62%; path 49 -> 62 -> 74 -> 84 -> 91 -> 96 -> 99 -> ~100%. R1 forecast is now capped at 95% of the benchmark prediction read on the real screen. (Fact 7, D.)
2. **Seller's market is now a priced branch (Branch S)**: a per-round capacity/demand ratio computed from FastTrack, a price ladder, and the NI value of each $1. Not in the base cash table because rival capacity is unknown. (C, E, PR4.)
3. **Honest leader/cost claims (B2)**: unit-leader and profit-leader from R3, below rival-average units in R2, cost-leading only through R6, not whole-market share leader without Stage 2 or Branch S. MTBF trim is shown to be break-even, not a CM lever.
4. **Two-tier worst-case cash test.** Tier 1 (as before) plus Tier 2: a miss 5 points worse than assumed must still leave cash >= $0 (no emergency loan). Funded by a standing current-debt buffer (R3 total $8.4M, 85% of the est. limit). NI and R5-R8 dividends are recomputed for the buffer interest.
5. **Echo launch year haircut**: R5 volume 525k (Apr 1 R5 revision), not 800k; cumulative Stage 2 NI falls from +$4.4M to +$2.9M; R4 funding and bond headroom re-checked.
6. **Capacity rule is stated per product line with a per-product volume table** (the pooled ratio column in rev 3 was misleading; the rule itself was always per line).
7. Kept (rebutted in the defense file): the per-line capacity increments, and bonds in R2-R3 (current debt cannot replace them once the Tier-2 buffer is funded).

**One-line strategy (contrarian).** The crowd will chase High Tech growth and cut LT prices. Erie holds LT price at the range ceiling, repositions Eat to the cheap trailing edge of LT, and uses the "share = CSS / sum of CSS" rule to build three LT products on separately financed lines. No equity dilution. High Tech only through a gated Stage 2. **Honest scope (rev 4): the base plan leads in profit, EPS and units from R3 and has the lowest unit cost through R6, but is NOT the whole-market share leader (16-23% total share) unless Stage 2 or Branch S fires. See B2.**

---

## 0. Rules audit: what checks out, and what is missing

Identities verified from your numbers:
- Capacity cost: 800k x ($6 + $4x3) = 800 x $18 = $14,400K = P&E. OK.
- Max stock issue: 20% x 2,000K sh x $11.17 = $4,468K. Max retire: 5% x 2,000K x $11.17 = $1,117K. OK.
- Max bonds: 80% x fixed assets $9,600K = $7,680K, minus existing bonds $5,200K = **$2,480K**. OK. (ASSUMPTION: 80% of NET fixed assets, since $9,600K is the net figure.)
- "Max investment $6,948K" = $4,468K + $2,480K exactly, so it is the stock cap plus the bond cap. **ASSUMPTION: whether unused stock headroom lets me spend more than bonds + cash is unverified; the plan has a fallback (Section C) and PR1 tests it.**
- Production 1,300 x 0.99 = 1,287 (A/P 30 days = 1% withheld). OK.
- A/R: $40.8M x 30/365 = $3,353K. OK.
- **Labor identity (the one used everywhere):** base labor at auto 3 = $11.20 - 2 x $1.12 = $8.96 first shift, $13.44 second shift. Check on your screen: 800 x 8.96 + 487 x 13.44 = $13,713K over 1,287 = $10.65 vs $10.60 shown. OK. For a 2nd-shift share m of units: **labor/unit = 8.96 x (1 + 0.5m)**. (ASSUMPTION: no annual wage raise in the plan; the brief says labor "rises with annual raise" but gives no rate. A 3% raise would add ~$0.3/unit per year and push CM down further. VERIFY on the PR proformas.)
- Unit cost $15.97 + $10.60 = $26.57; CM = (34 - 26.57)/34 = 21.9% vs screen 21.8%.
- Leverage: equity = 20,907 - 2,853 - 5,200 = 12,854; 20,907/12,854 = 1.63 vs 1.6. OK.
- **Working-capital ratio (sourced, used in every cash roll):** R0 (A/R 3,353 + inventory 2,352 - A/P 2,853) / sales 40,800 = 2,852/40,800 = **7.0%**.
- **Current-debt limit** (brief: (75% of A/R + ~15% of last year's direct labor + material) x 1.2). Sales = units x $35, A/R at 30 days. R1 ~$9.2M, R3 ~$9.9M, R4 ~$13.8M (ASSUMPTION: last-year direct cost = units x VC; VERIFY on the Finance screen).

**Not in the brief (placeholders only, all marked):**
1. How CSS combines criteria with awareness and accessibility. I use CSS ~ (sum of weight x criterion score) x (1+aw)/2 x (1+acc)/2, only for RATIOS.
2. Tax, SG&A, interest on old bonds. Calibrating to R0: "SG&A 2% of sales, tax 35%, interest 10%" gives NI $2.51M vs $2.49M actual. On the default R1 case the same model gives $2.66M vs the screen's EPS $1.05 x 2,000K = $2.10M, so **my NI runs ~$0.5M/yr high (sourced from the brief's own R1 screen: EPS $1.05 x 2,000K = $2.10M vs model $2.66M). Every NI figure below is already cut by $0.5M.** I cannot build a real P&L (the brief gives no SG&A or tax rate), so dividend dollars below are placeholders: at each save set dividend = min(proforma EPS, allowed distributions from the proforma worst-case). VERIFY on proformas.
3. The material-cost surface beyond the book's listed points (slope ~$2.0-$4.0 per Pfmn unit; ~$2.5 for later moves).
4. HR/TQM effects, annual wage raise, when new capacity starts depreciating (assumed the year after purchase).
5. Whether capacity can be added to an existing line (assume yes, $6 + $4 x auto per unit) and when automation changes take effect (assume next year).
6. LT age scoring below 2.2 and above 3.1 (only 2.2 -> 91 and ~3.0 -> 96 are given), and how multiple simultaneous projects lengthen R&D.
7. What the 5 rivals do (Section A is inference).
8. Existing bonds ($867K due 2028 = R2, $1,733K due 2030 = R4, $2,600K due 2032 = R6) are ASSUMED repaid from cash at maturity, not refinanced.
9. The promo response below $1.5M. The brief gives only $1.5M -> ~+36 awareness points and $3M -> just under +50. **ASSUMPTION: $1.0M -> ~+24 points (linear scaling of the $1.5M point; the real curve is probably concave, so this is conservative).** PR1 measures it.
10. Whether the 1/12-per-month launch ramp is measured on first-shift capacity only (assumed) and whether a stock-out sends customers to our other product or to a rival (unknown).

---

## A. Diagnosis: the 8 facts that decide this market

1. **Eat sits between segments; the book says one repositioned product cannot be both well positioned and young enough for HT.** Eat is 0.42 from the R1 HT center (6.7/13.3), 1.56 from the LT ideal (5.3/14.7), but 2.40 from the R1 HT ideal (8.1/11.9); HT revision for Eat = Apr 19 NEXT year. HT needs a NEW product; LT can be won with Eat.
2. **LT is the profit pool early and stays big.** Demand (k): LT 5,544 (R1) -> 10,804 (R8) at 10%/yr; HT 2,592 -> 9,287 at 20%/yr (ASSUMPTION: rates unchanged; FastTrack can change them). LT is 68% of demand in R1, 54% in R8. LT position is only 9% of the score. HT overtakes LT after R8 and is 46% of R8 demand, which is why Stage 2 (C2) exists.
3. **Material cost is the biggest controllable lever.** Moving to 5.3/14.7 with MTBF 20,000 cuts material from $15.97 to ~$12.00 (book): **-$3.97/unit x ~1,200k = ~$4.8M/yr** for ~$0.86M of R&D (313/365 x $1M). R1 default CM 21.8% becomes ~36% at $35 once fully effective. The lever decays as the drift forces repositioning up the cost curve (blended material $12 -> $17 by R8), which is why CM falls later.
4. **Capacity is the scarce asset early, the 2nd shift is the cheap buffer later.** A line takes a full year to buy; R1 limit $6,948K buys 6,948/18 = **386k** at auto 3. Industry first-shift capacity today is 6 x 800 = 4,800k (9,600k with 2nd shift) vs R1 demand 8,136k. If the 5 rivals do not expand, industry capacity including 2nd shift is 5 x 2 x 800 = 8,000k + ours 2 x 1,900 = 3,800k = 11,800k in R5 vs R5 demand 13,492k (ratio 0.87), a seller's market from about R4 (11,540k vs 11,856k = 0.97). If two rivals each add ~380k the R5 ratio is ~0.99 and there is none. Branch S in C turns this into a price rule (VERIFY the size of the "$9.99 above range" effect). **A unit of first-shift capacity costs $18 and saves only $4.48/yr (0.5 x $8.96) when it merely displaces 2nd-shift hours, but earns ~$16-18/yr when it is the only way to build the unit** (first-shift CM ~$11 + 2nd-shift CM ~$6.5 at R5). So lines are bought only as volume requires.
5. **Share is additive in product count, but only at near-parity CSS, and new products start behind.** Share = own CSS / sum of CSS. With r effective LT rivals (ASSUMPTION r = 4; 5 identical rivals each have one LT-selling product, some will leave), n products with relative CSS k give share nk/(nk+r):

| n products | k=1.0, r=4 | k=0.8, r=4 | k=0.6, r=4 | k=1.0, r=5 | k=1.0, r=3 |
|---|---|---|---|---|---|
| 1 | 20.0% | 16.7% | 13.0% | 16.7% | 25.0% |
| 2 | 33.3% | 28.6% | 23.1% | 28.6% | 40.0% |
| 3 | 42.9% | 37.5% | 31.0% | 37.5% | 50.0% |

   **Time-varying k (derived from the awareness rule, Section C model).** A new product launches at 25% free awareness + ~24 points from $1.0M = ~49%, CSS awareness factor (1+0.49)/2 = 0.75, vs Eat's ~0.92 by R2: ratio 0.82; times an ASSUMED age discount of 0.85 for an age-0.5 product against an LT peak of ~3.0 = **k ~0.70 in the launch year, ~0.85 in year 2, ~0.95 from year 3.** Two or more products in a fine cut are also needed for 100% accessibility. A one-product rival cannot copy this inside a year. **Capex beyond the first two lines goes through gates that measure k (Section C).**
6. **Price is a weak lever in LT; MTBF is a strong one.** LT price points: $15 -> 100, $20 -> 70, $25 -> 40, $30 -> 20, $35 -> 1; weight 41%. MTBF: +1,000 hrs in range = +16.5 pts x 0.21 = 3.5 base points, worth ~$1.4-$2.1 of price, for $0.30 of cost. So **price at the ceiling, MTBF at the top (20,000)**. Full margin test in B.
7. **Awareness does NOT reach 100% quickly; budget it with the decay rule.** Awareness starts each year at last year x 2/3, then $1.5M adds ~36 points. Eat (55% today): R1 start 36.7% -> ~73% at $1.5M; R2 start 48.5% -> ~85%; R3 start 56.3% -> ~92%; R4 start 61.5% -> ~97%; R5 ~100% (cap). CSS factor (1+aw)/2: 0.86, 0.92, 0.96, 0.99. $3M instead of $1.5M gets Eat to ~86% in R1 (+7.7% CSS on one product of three = ~+60k units x $12 = $0.7M) for +$1.5M cost, so $1.5M is right, $3M is not. **Accessibility follows the same decay rule (rev 4 fix).** Start = last year x 2/3, then add g(budget): g($1M) ~ +13 (it holds the R0 40% against a 13.3-point decay), g($2M) = +22 (brief), g($3M) ~ +29 (ASSUMPTION, interpolated), g($3.5M) = +33 (brief: ~$3.5M maintains 100%), g($4M) ~ +35 (brief). Path: R1 $2M: 26.7 + 22 = **49%** (factor 0.745, not 62%); R2 $3M: 32.5 + 29 = 62%; R3 $3.5M: 41 + 33 = 74%; R4 $4M: 49 + 35 = 84%; R5 91%; R6 96%; R7 99%; R8 ~100% (the top needs 2+ products in the fine cut). Factors (1+acc)/2: 0.745, 0.81, 0.87, 0.92, 0.955, 0.98, 0.995; rivals on defaults hold 40% (0.70). Return on the second $1M in R1: 0.745/0.70 = +6.4% CSS = ~+60k units x $9.1 = ~$0.55M in R1 alone, but 2/3 of the gain carries into each later year (R2-R8 add about $1.5M), so about 2x the $1.0M: keep $2M and let the PR1 experiment (sales $1M/$2M/$3M) measure it. The plan's R2+ units come from the awareness/age ceiling and do not bank any accessibility edge over rivals; that is unmodeled upside.
8. **Likely rival behavior (inference), R1-R3:** (a) some leave defaults; (b) some reposition Eat toward HT (arrives ~Apr 19 R2, age ~2.9 at year-end); (c) some cut LT price to $25-$30; (d) some buy ~380k with max stock + bonds, arriving R2; (e) a few trigger emergency loans.
   **Exploit:** do not follow price cuts (B); rivals fleeing LT raise our LT share; nobody has 2+ LT products before R3, so we alone can reach the 2+ product accessibility ceiling (path 49% -> ~100% by R8, fact 7); read rival capacity every round (E).

---

## B. Strategy choice

**Chosen: Niche Cost Leader (LT) with a multi-product wall.** Three LT lines (Eat, Ease, Edge), all at the trailing-edge cost position. Price is held at the ceiling, so the "cost" edge shows up as CM, not as a low price.

### B1. The alternatives, costed on one basis (contribution per $ of line capacity per year, $18 per unit at auto 3; R3 labor from the single formula)

| Strategy | Unit economics | Per-year contribution per $ of line | Verdict |
|---|---|---|---|
| **Chosen: Niche Cost Leader, LT wall at $35** | R3: VC $23.2 -> CM $11.8 (34%). Early lines (needed for units): first-shift CM $11-12 + 2nd-shift CM $6.5 | $11.8/$18 = **0.65** on average; **~1.0** for a line that unlocks units; 0.25 for slack (rule in C) | Payback ~1.5 yrs |
| Alt A: price-cut Cost Leader (same LT wall at $32 / $30 / $25) | R3 base 2,050k units at $35 = $24.1M. $32: price score ~12 (+4.7 base, ~+8% CSS) -> share 44.8%, units x1.045 = 2,142 x $8.8 = **$18.8M**. $30: +14% CSS, x1.074 = 2,202 x $6.8 = **$14.9M**. $25: +28% CSS, x1.145 = 2,347 x $1.8 = **$4.2M** | $8.8/18 = 0.49; 0.38; 0.10 | Rejected. The table is generous to the cut (lets units rise freely) and it still loses |
| Alt B: Niche Differentiator (HT), snapshot at R3 | New product (earliest R3 launch). Material ~$19.3 + labor $10.35 = VC ~$29.7; price $40 (HT price score ~20) -> CM $10.3 (26%). HT R3 demand 3,732k x 20% = 746k -> $7.7M; yearly repositioning ~0.7 units ~$1M/yr = -$1.3/unit | ($10.3 - $1.3)/$18 = **0.50**; capex 746 x $18 = $13.4M, bought in R2 | Rejected AS A R3 LAUNCH (cash cannot fund it with the LT wall). **Re-costed for R5-R8 in C2, where it is adopted as a gated Stage 2** |
| Alt C: Differentiator with Product Lifecycle Focus (launch HT, age into LT) | Same HT years R3-R5 at 0.50. From R6 the product at 8.1/11.9 sits 0.42 from the LT center (7.8/12.2) but its material is ~$18.4 (extrapolated from the book's 7.4/12.6 = $17.24 and 6.9/13.1 = $16.44, slope ~$1.6 per 0.5 Pfmn) + labor ~$10.4: CM at $35 = $6.2 (18%) | LT phase $6.2/$18 = **0.34** | Rejected: the "aging" phase earns about half the margin of a product built at the trailing edge, and a 4+ year-old product is past the LT age peak (3.0) |
| Alt D: Broad Differentiator (LT wall + HT product) | = Chosen + Stage 2 overlay (C2) | marginal HT dollar 0.18-0.25 after marketing, 0.60 before | Adopted only as a gated Stage 2 from R4 |
| Default Eat, no change | CM 21.8%, NI ~$2.1M | - | Not a leader |

**Marginal test of a price cut** (answers "is $35 simply the corner solution?"). At n=3, k=1, d(share)/dk = 12/(3k+4)^2 = 0.245. A $1 cut near the top gains 3.8 pts x 0.41 = 1.56 base points; against a ~56-point base (ASSUMPTION) that is +2.8% CSS -> +0.69 share pts -> +1.6% units = +33k units x $11.8 = **+$0.4M**, but costs $1 x 2,050k = **-$2.05M**. Even if the base is only 30 (gain x1.87), the gain is $0.73M vs $2.05M cost. The cut loses at every base I can defend (VERIFY with the PR3 A/B).

**Capacity vs automation (recomputed with the correct mix).** Per unit of first-shift line capacity C, produced volume is C x (1 + u), u = 2nd-shift utilization (0 to 1). An automation point saves $1.12 per first-shift unit and $1.68 per 2nd-shift unit: C x (1.12 + 1.68u). It costs $4C. At u = 0.77 (R7: 3,900/2,200 = 1.77x) that is $2.41 per $4 = **1.7-year payback**; at u = 0.4 it is 2.2 years. This is better than slack capacity (4 years) but it lengthens R&D and its timing is unknown (Section 0). **Decision: automation 3 -> 4 on Eat only, as a gated option at R5 (bought R5, active R6)**: 800 x $4 = $3,200K, saves 800 x (1.12 + 1.68 x 0.66) = $1.8M/yr, 3 years R6-R8 = $5.4M vs $3.2M. Gate: PR3 shows automation does not delay a reposition past Dec 1 and the worst-case cash test passes. Not in the base cash table.

**Barriers rivals cannot copy:** (i) capacity bought a year ahead, capped by ~$7M-$12M/yr of headroom per rival: we reach 1,375k effective first shift by R3 and 2,200k by R7, vs 800k-1,200k for a rival; (ii) 100% accessibility needs 2+ products in the fine cut; (iii) cost: -$4/unit material in the early years; (iv) awareness: Eat reaches ~92% by R3 and ~100% by R5 at $1.5M, while a rival who skimps on promo decays by a third a year.

**Scoring.**
- **Rank-based** (profit, EPS, stock price, ROE, share): NI ~$4.8M (R2), $6.5M (R3), $9.2M (R5), $8.1M (R8) vs $2.5M today (after the Tier-2 buffer interest, see C); EPS $4.05 in R8 vs $1.25 today. NI peaks in R6 and slides because rising material cost (the drift) outruns the flat $35 price. With Stage 2 (re-costed in C2): EPS ~$4.95 in R8. With Branch S, each +$1 of LT price is worth ~$1.8M (R4) to ~$2.6M (R8) of NI.
- **BSC.** Financial: profit up, leverage peaks ~R3-R4 (current debt $8.4M in R3 incl. the Tier-2 buffer, plus bonds; a cost of the worst-case insurance). Internal: CM 34% R3 -> 30% R4 -> 28% R5 -> 20% R8 (below the 30% slide target from R5); plant utilization high (2nd shift 35-45% of units). Customer: accessibility 49% (R1) -> 84% (R4) -> ~100% (R8), awareness 85-100%, product line of 3. L&G (HR): unknown; tested in PR2-PR5.
- **Conflicts:** (1) 2nd shifts lower CM and "days of working capital"; (2) end-game dividends/retirements help rank (stock price) but shrink the equity buffer; (3) worst-case insurance borrows short-term debt (pre-tax interest on the Tier-2 buffer: $0.20M R3, $0.28M R4, $0.46M R8) and raises leverage, a BSC Financial cost; (4) the $35 price may cap the share that share-rank graders reward (our total share is 16-23%, near the 16.7% parity; only Stage 2 moves it to ~28%); (5) Stage 2 raises EPS and share but cuts CM% and R5-R6 dividends and adds leverage. **Tie-break:** under uncertainty prefer profit and stock price (rank-safe); keep CM >= 28% where cheap. The MTBF trim (E) is the first CM lever.

---

### B2. What "leader" means here, and where the plan is weak (rev 4)

**Unit leadership vs the average rival** (ASSUMPTION: rivals split the rest of total demand evenly; if rivals are capacity-capped at 2 x 800 = 1,600k each without expansion, our lead is larger):

| R | Our units | Total demand | Avg rival units | Ours / rival |
|---|---|---|---|---|
| 2 | 1,500 | 9,208 | 1,542 | **0.97x (below average; Ease launches late)** |
| 3 | 2,050 | 10,440 | 1,678 | 1.22x |
| 4 | 2,750 | 11,856 | 1,821 | 1.51x |
| 5 | 3,100 | 13,492 | 2,078 | 1.49x |
| 8 | 4,000 | 20,091 | 3,218 | 1.24x |

So "dominant" holds for profit, EPS and units from R3, not for R2 and not for total share (16-23%, parity 16.7%). Whole-market share dominance needs Stage 2 (R8 27.6%) or a rival collapse.

**Cost leadership is real only through R6.** Our VC per unit (C table): R2 22.5, R3 23.2, R4 24.4, R5 25.3, R6 26.2, R7 27.2, R8 28.0, vs the untouched default 26.57. A rival that also repositions faces the same drift cost path (unknown), so the R7-R8 comparison is open. R8 CM 20.1% is below the 21.8% default. Levers, in order: (1) Branch S price when the seller's ratio allows (+$3 at $38: R8 CM (38-28)/38 = 26.3%); (2) delay a reposition; (3) the MTBF trim is NOT a profit lever: trimming 3,000 hrs saves $0.90 x 1,333k = $1.2M, but LT MTBF score falls 3 x 16.5 = 49.5 pts x 0.21 = 10.4 base pts of ~56 (ASSUMPTION) = -18.6% CSS on that product (weight 0.97 -> 0.79, total share 42.1% -> 40.6%, -162k units x $7.0 = -$1.1M); 1,000 hrs is also break-even ($0.40M saved vs ~$0.38M lost). Use it only to meet a BSC CM target.

---

## C. Round-by-round plan

**Planning-model assumptions (all ASSUMPTION; replace with proformas).** LT demand +10%/yr; r = 4 effective LT rivals; price $35 flat; promo $1.5M per product at steady state ($1.0M in a new product's launch year, 25% free awareness); sales budget $2.0M (R1), $3.0M (R2), $3.5M (R3), $4.0M (R4+); SG&A 2% of sales; tax 35%; depreciation = prior-year-end P&E / 15; NWC = 7.0% of sales at A/R 30 days; **labor per unit = 8.96 x (1 + 0.5m)**; blended material R1 $15.4, R2 12.3, R3 12.8, R4 13.8, R5 14.6, R6 15.4, R7 16.3, R8 17.0 (+~$2.5 per Pfmn unit as we reposition); dividends $0.25/sh = $500K in R2-R3. NI for R3-R8 = rev-2 NI adjusted for the change in contribution (new units x CM vs old), depreciation, interest and R&D, at 65% after tax; I did not rebuild a full P&L because the brief gives no SG&A or tax rate.

**New-product timing.** Brief: invention takes >= 1 year; production starts only after the revision date; max 1/12 of annual capacity per month. Ease starts Jan 1 R1, so it cannot sell before Jan 1 R2. With two simultaneous projects in R1 I assume the revision slips: **ASSUMPTION Ease revision Apr 1 R2, Edge Apr 1 R3.** Launch-year output = months x (1/12 x line capacity): Ease 9 x 31.7 = **285k**; Edge (260k line) 9 x 21.7 = **195k** (VERIFY whether the 2nd shift raises this). **Sensitivity to a late revision (Ease, 380k line, pre-tax):** Apr 1 = 285k (plan); Jul 1 = 190k, -95k units = **-$1.1M**; Oct 1 = 95k, -190k units = **-$2.3M**. Both are covered by the -20% worst-case volume used in R2-R3.

**Worst-case cash test (one definition, every round).** Production is fixed at the BEST-case forecast, so a volume shortfall of s% leaves units built and paid for. Cash lost per unit not sold = revenue not collected within the year + carrying on the extra stock - tax shield:
**L = $35 x (1 - 30/365) - 0.35 x CM + 0.65 x 0.12 x VC = $32.12 - 0.35 CM + 0.078 VC.**
Example R2 (CM $12.5, VC $22.5): 32.12 - 4.38 + 1.76 = **$29.50 per unit**. Inventory will exceed the 1/6 rule in that scenario; it is a TEST, not a plan. ASSUMPTION on s: R1 15%, R2-R3 20%, R4 15%, R5-R8 10%. Re-run on the real proformas before every save.
**Tier 2 (rev 4).** s is itself an assumption, so a second test uses s + 5 points (R1 20%, R2-R3 25%, R4 20%, R5-R8 15%) and must leave Dec 31 cash >= $0 (no emergency loan). The extra loss is 5% x plan units x L. Funded by a standing current-debt buffer X (table below the cash math). Beyond Tier 2 the tail is priced, not hidden: a miss 10 points past Tier 2 in R5 is 310k x $30.69 = $9.5M short, at 8.6% + 7.5% = 16.1% for a year = ~$1.5M interest plus the stock-price hit; accepted knowingly.

**Pre-funding rule.** If worst-case Dec 31 cash < $1.0M, add current debt (8.6%, no fee, repayable each Jan 1) until it is >= $1.0M, up to the current-debt limit; only if that is exhausted, cut in the flex order (dividend, automation, Edge top-up, promo). Extra debt sits as cash in the base case; its cost (8.6% x 0.65) is already in NI and cash below.

**Capacity rule (replaces rev 2's expansion schedule).** For each product line (never the pooled total: each product has its own line, and its volume is its CSS-weight share of plan units, see the per-product table below), next-year production P = forecast x ~1.01 (steady-state inventory). Buy first-shift capacity so that P <= 1.85 x that line's first-shift capacity. Eat is the overflow line: it has slack to 1.85 x 800 = 1,480k. Reason: a line that is needed to build units earns ~1.0 per $ per year; a line that only displaces 2nd-shift hours earns $4.48/$18 = 0.25 (payback 4 years, worse than dividends once the stock-price rule is applied). Eat is never expanded (its 800k line covers 1.7x of its share to R8). The last purchase is R6 for R7 (two years of use); no R7 purchase unless the gate below fires.

**Plan units (k, all segments) and lines (first shift, k):**

| R | Plan units | Eat | Ease | Edge | Total first shift | Pooled units / pooled first shift (information only, NOT the rule) |
|---|---|---|---|---|---|---|
| 2 | 1,500 | 800 | 380 (285 in year) | - | 1,085 | 1.38 |
| 3 | 2,050 | 800 | 380 | 260 (195 in year) | 1,375 | 1.49 |
| 4 | 2,750 | 800 | 520 | 450 | 1,770 | 1.55 |
| 5 | 3,100 | 800 | 550 | 550 | 1,900 | 1.63 |
| 6 | 3,500 | 800 | 625 | 625 | 2,050 | 1.71 |
| 7 | 3,900 | 800 | 700 | 700 | 2,200 | 1.77 |
| 8 | 4,000 | 800 | 700 | 700 | 2,200 | 1.82 |

R8 is held at 4,000 (not rev 2's 4,200) because 2 x 2,200 = 4,400 is the hard ceiling and best-case production (4,000 x 1.09 = 4,364) must still fit. The demand ceiling for R8 is 4,550, so R8 is the one capacity-bound round.

**Per-product volumes vs lines (this is the rule as applied; volume = plan units x CSS-weight share from the demand-ceiling table: R3 .393/.332/.275, R4 .358/.339/.303, R5-R7 .345/.327/.327, R8 1/3 each; launch years are supply-limited):**

| R | Eat units (line 800) | Ease units (line) | Edge units (line) | Ease ratio | Edge ratio | Rule |
|---|---|---|---|---|---|---|
| 2 | 1,215 (1.52x) | 285 (380, 9 months) | - | launch | - | Eat absorbs the supply-limited launch (stock-out rule; VERIFY the overflow goes to Eat, not a rival) |
| 3 | 1,155 (1.44x) | 700 (380) | 195 (260, 9 months) | 1.84x | launch | Ease at the limit, so +140 for R4 |
| 4 | 984 (1.23x) | 934 (520) | 832 (450) | 1.80x | 1.85x | fires for both |
| 5 | 1,070 (1.34x) | 1,015 (550) | 1,015 (550) | 1.85x | 1.85x | fires for both |
| 6 | 1,208 (1.51x) | 1,146 (625) | 1,146 (625) | 1.83x | 1.83x | fires for both |
| 7 | 1,346 (1.68x) | 1,277 (700) | 1,277 (700) | 1.82x | 1.82x | gate only |
| 8 | 1,333 (1.67x) | 1,333 (700) | 1,333 (700) | 1.90x | 1.90x | the one bound round (limit 2.0x) |

Each increment bought (Ease 380 -> 520 -> 550 -> 625 -> 700; Edge 260 -> 450 -> 550 -> 625 -> 700) is the smallest that brings that line to <= 1.85x. Rev 3 printed only the pooled ratio (1.38-1.82), which made the rule look unfired; it is per line, and Eat (never expanded) carries up to 1.68x.

NI and cash columns in the next table are PRE-overlay; the Tier-2 overlay (below the cash math) lowers NI by the buffer interest and adds the standing current-debt buffer.


| R | Year | R&D (Jan 1 starts) | Promo each / sales budget | Capex now (buys next-year capacity) | Financing | Units | VC | CM | NI $M (pre-overlay) | End cash $M (base / Tier-1 worst), pre-overlay |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2027 | Eat -> 5.3/14.7 MTBF 20k (rev ~Nov 9). New Ease 5.5/14.5 MTBF 20k | Eat 1,500 / 2,000 | Ease line 380 @auto 3 = **6,840** | Bonds 2,480; current debt **4,000**; stock 0; div 0 | 1,175 (850 LT + 325 HT) | 25.9 | 26% | 1.0 | **6.98 / 1.56** (s = 15%) |
| 2 | 2028 | New Edge 5.9/14.1 MTBF 20k | Eat 1,500; Ease 1,000 / 3,000 | Edge line **260** @3 = **4,680** (not gated) | Bonds 2,500; current debt 5,100 (roll 4,000 + 1,100); pay 867 maturity; div $0.25 | 1,500 | 22.5 | 12.5 (35.7%) | 4.9 | **9.86 / 1.01** (s = 20%) |
| 3 | 2029 | Eat -> 5.9/14.1 (rev ~May) | Eat 1,500; Ease 1,500; Edge 1,000 / 3,500 | Ease +140 = 2,520; **Edge +190 = 3,420 (gated)**; total **5,940** | Bonds 2,000; current debt 6,100 (roll 5,100 + 1,000); div $0.25 | 2,050 | 23.2 | 11.8 (33.6%) | 6.6 | **13.26 / 1.03** (s = 20%) |
| 4 | 2030 | Ease -> 6.3/13.7 | 1,500 x3 / 4,000 | Ease +30 = 540; Edge +100 = 1,800; **= 2,340** | No bonds; pay 1,733 maturity; repay current debt 1,500 (4,600 left); div $0.50 | 2,750 | 24.4 | 10.6 (30.4%) | 6.7 | **13.83 / 1.32** (s = 15%) |
| 5 | 2031 | Eat -> 6.9/13.1; Edge -> 6.9/13.1 | same | Ease +75, Edge +75 = **2,700** | Repay current debt 4,600 (0 left); div $3.40 (6,800) | 3,100 | 25.3 | 9.7 (27.7%) | 9.4 | **10.55 / 1.04** (s = 10%) |
| 6 | 2032 | Ease -> 7.4/12.6 | same | Ease +75, Edge +75 = **2,700** | Pay 2,600 maturity; div $2.25 (4,500) | 3,500 | 26.2 | 8.8 (25.1%) | 9.7 | **11.93 / 1.05** |
| 7 | 2033 | Eat -> 7.4/12.6; Edge -> 7.4/12.6 (~$0.34M each) | same | **0** (gate: +50/+50 = 1,800) | div $4.35 (8,700 = EPS) | 3,900 | 27.2 | 7.8 (22.3%) | 8.7 | **13.59 / 1.30** |
| 8 | 2034 | none (no payback) | same | 0 | div $4.20 (8,400 = EPS); retire stock ~2,000 (cap permitting) | 4,000 | 28.0 | 7.0 (20.1%) | 8.4 | **~13.8 / ~1.05** |

**Reposition schedule and distance check (every product stays inside ~2.0 of the LT center through R8).** Distance = 1.414 x |Pfmn gap| to the end-of-year LT center (diagonal Pfmn + Size = 20); trigger 2.1, fine cut 2.5. Ages are approximate (reposition halves age; MTBF-only changes do not).

| Year-end | LT center Pfmn | Eat (spec; dist) | Ease (spec; dist) | Edge (spec; dist) |
|---|---|---|---|---|
| R1 | 5.3 | 5.3; 0.0 | - | - |
| R2 | 5.8 | 5.3; 0.7 | 5.5; 0.4 | - |
| R3 | 6.3 | 5.9; 0.6 | 5.5; 1.1 | 5.9; 0.6 |
| R4 | 6.8 | 5.9; 1.3 | 6.3; 0.7 | 5.9; 1.3 |
| R5 | 7.3 | 6.9; 0.6 | 6.3; 1.4 | 6.9; 0.6 |
| R6 | 7.8 | 6.9; 1.3 | 7.4; 0.6 | 6.9; 1.3 |
| R7 | 8.3 | 7.4; 1.3 | 7.4; 1.3 | 7.4; 1.3 |
| R8 | 8.8 | 7.4; **2.0** | 7.4; **2.0** | 7.4; **2.0** |

Eat age path: 2.1 (R1 end), 3.1, ~2.4 (R3 move), 3.4, ~2.6 (R5 move), 3.6, ~2.6 (R7 move), 3.6: never above ~3.6, so the age-4.5 trigger never fires. Moves of 0.5 Pfmn take ~5 months and ~$340K (book); the R6 Ease move of 1.1 is ~Sep-Oct (book: 1.0 move = Sep 25, $744K) and its late revision is tolerated because Ease is only 1.4 off at mid-year. Two simultaneous projects (R5 Eat+Edge, R7 Eat+Edge) may slip: if the R&D screen shows a revision after Oct 15 for either, run the other in the previous year. R7 moves cost ~$0.68M pre-tax and are in R7 NI (-$0.44M).

**Demand-ceiling check.** LT-only ceiling = LT demand x (sum of our weights)/(sum + 4), our weights = k x 0.97 (the ~3% CSS penalty of a $35 price against a rival at $34), k = 0.70 / 0.85 / 0.95 by product age as in A5. Plan units are a forecast haircut to this upper bound (82-92%), NOT a capacity bound in R2-R7:

| R | Our weights | Share | LT demand | Ceiling | Plan units (all segments) | Plan / ceiling |
|---|---|---|---|---|---|---|
| 2 | 0.97 + 0.68 = 1.65 | 29.2% | 6,098 | 1,780 | 1,500 | 84% |
| 3 | 0.97 + 0.82 + 0.68 = 2.47 | 38.2% | 6,708 | 2,560 | 2,050 | 80% |
| 4 | 0.97 + 0.92 + 0.82 = 2.71 | 40.4% | 7,379 | 2,980 | 2,750 | 92% |
| 5 | 0.97 + 0.92 + 0.92 = 2.81 | 41.3% | 8,117 | 3,350 | 3,100 | 93% |
| 8 | 2.91 | 42.1% | 10,804 | 4,550 | 4,000 | 88% (capacity-bound at 4,400) |

With r = 5 rivals the R8 ceiling is 2.91/7.91 = 36.8% x 10,804 = 3,975k, i.e. plan is about at the ceiling; the plan still earns a profit and passes the cash gate. Share of total market: R2 1,500/(6,098+3,110) = 16.3%; R5 3,100/13,492 = 23.0%; R8 4,000/20,091 = 19.9%; LT-only R3 2,050/6,708 = 31%; R8 ~37%. **The base plan leads LT, not the whole market; its total share is 16-23% (parity is 16.7%) and falls in R8 as HT grows to 46% of demand. C2 addresses that.** 2nd-shift usage (units beyond first shift, as a share of first-shift capacity): R3 49%, R5 63%, R8 82% (limit 100%).

### Branch S: seller's market pricing (rev 4; NOT in the base cash table)

Rule: if industry capacity (incl. 2nd shift) cannot meet a segment's demand, even poor products in the rough cut sell and prices up to $9.99 above range sell. Our units are then capacity-limited, not CSS-limited, so extra price is margin, not lost share.

**Seller's ratio (each round, from FastTrack; VERIFY it shows rival capacity):** (sum of rivals' 2 x next-year first-shift capacity + our 2 x first shift) / next-year total demand. ASSUMPTION: compared in total; LT-only is lower still if rival capacity sits in HT-positioned lines.

| Scenario | R3 | R4 | R5 | R6 | R7 | R8 |
|---|---|---|---|---|---|---|
| Demand (k) | 10,440 | 11,856 | 13,492 | 15,379 | 17,562 | 20,091 |
| Capacity, rivals stay at 800 (8,000k) + ours (2 x 1,375 ... 2 x 2,200) | 10,750 | 11,540 | 11,800 | 12,100 | 12,400 | 12,400 |
| **Ratio, no rival expansion** | 1.03 | **0.97** | **0.87** | **0.79** | **0.71** | **0.62** |
| Ratio, two rivals +380 each from R2 (capacity +1,520) | 1.18 | 1.10 | 0.99 | - | - | - |

**Ladder (ASSUMPTION thresholds; brief allows up to +$9.99 but gives no CSS cost curve):** ratio >= 1.00: $35; 0.90-1.00: $36; 0.75-0.90: $37; < 0.75: $38; cap +$4 until PR4 data. All three LT products together. Step back $1 if year-end inventory > 1/6 of available units. Re-run both cash tiers with L recomputed at the new price (L = 0.918 P - 0.35 CM + 0.078 VC).

**Value (after tax, per +$1, on plan units):** R4 2,750k x $0.65 = $1.8M; R5 $2.0M; R6 $2.3M; R7 $2.5M; R8 $2.6M. If rivals do not expand (ladder +$1 R4, +$2 R5, +$3 R6-R8): pre-tax 2.75 + 6.2 + 10.5 + 11.7 + 12.0 = $43M, ~$28M after tax; R6 CM would be (38-26.2)/38 = 31%. This is UPSIDE only; if two rivals expand it is zero. Because it depends on rivals, the base plan keeps $35.

### Cash math (every round; includes bond maturities, tax shield, A/R relief and carrying cost)

R1 ($K): 5,602 + NI 1,000 + dep 960 (14,400/15) - NWC build 100 - capex 6,840 + bonds net 2,356 (2,480 x 0.95) + current debt 4,000 = **6,978**. Worst (s = 15%, 175k units, CM $9.1, VC 25.9): L = 32.12 - 3.19 + 2.02 = $30.95 x 175 = **5,416** -> **1,562**. Capex $6,840K <= $6,948K cap. Current debt limit ~ (0.75 x 3,353 + 0.15 x 34,200) x 1.2 = ~$9.2M, so $4.0M fits.

R2: 6,978 + NI 4,900 + dep 1,416 (21,240/15) - NWC 798 (7% x (52.5 - 41.1)M) - capex 4,680 + bonds net 2,375 - div 500 - maturity 867 = **8,824** before insurance. Worst (s = 20%, 300k x $29.50) = **8,850** -> **-26**: add current debt 1,100 (after-tax interest 62): base **9,862**, worst **1,012**. Bond limit: net FA at R2 start = 21,240 - 5,760 = 15,480; x80% = 12,384; bonds outstanding 7,680 -> headroom 4,704 >= 2,500. OK.

R3: 9,862 + NI 6,610 + dep 1,728 (25,920/15) - NWC 1,348 (7% x (71.75 - 52.5)M) - capex 5,940 + bonds net 1,900 - div 500 = **12,312** before insurance. Worst (s = 20%, 410k; CM $11.77, VC $23.23: L = 32.12 - 4.12 + 1.81 = $29.81 x 410 = **12,222**) -> **90** -> add current debt 1,000 (after-tax interest 56): base **13,256**, worst **1,034**. Current debt 6,100 vs limit ~$9.9M. Bond check: FA = 25,920 - 7,176 = 18,744; x80% = 14,995; bonds after R2 = 9,313 -> headroom 5,682 >= 2,000. **Skipping the gated Edge increment** (3,420) raises worst-case cash by 3,420 and lets current debt drop by ~1,000.

R4: 13,256 + NI 6,740 + dep 2,124 (31,860/15) - NWC 1,715 (7% x 24.5M) - capex 2,340 - maturity 1,733 = **16,332**. Worst (s = 15%, 413k; CM $10.64, VC $24.36: L = 32.12 - 3.72 + 1.90 = $30.30 x 413 = 12,514) -> **3,818**. Surplus: repay current debt 1,500 and pay a $0.50 dividend (1,000): base **13,832**, worst **1,318**. Bond check: FA = 31,860 - 8,904 = 22,956; x80% = 18,365; bonds = 11,313 -> headroom 7,052 (no issue needed).

R5: 13,832 + NI 9,400 + dep 2,280 (34,200/15) - NWC 858 - capex 2,700 = 21,954; repay current debt 4,600 -> 17,354. Worst (s = 10%, 310k; CM $9.71, VC $25.29: L = 32.12 - 3.40 + 1.97 = $30.69 x 310 = 9,514). Allowed distributions = 17,354 - 1,000 - 9,514 = 6,840; dividend $3.40 = 6,800 (EPS $4.70) -> base **10,554**, worst **1,040**.

R6: 10,554 + NI 9,700 + dep 2,460 (36,900/15) - NWC 980 - capex 2,700 - maturity 2,600 = 16,434. Worst (s = 10%, 350k; CM $8.78, VC $26.22: L = 32.12 - 3.07 + 2.05 = $31.10 x 350 = 10,885). Allowed = 4,549; dividend $2.25 = 4,500 (EPS $4.85) -> base **11,934**, worst **1,049**.

R7: 11,934 + NI 8,700 + dep 2,640 (39,600/15) - NWC 980 = 22,294. Worst (390k; CM $7.79, VC $27.21: L = 32.12 - 2.73 + 2.12 = $31.51 x 390 = 12,289). Allowed = 9,005; dividend $4.35 = 8,700 (= EPS) -> base **13,594**, worst **1,305**. If the capacity gate fires (+1,800), allowed = 7,205 and the dividend becomes $3.60.

R8: 13,594 + NI 8,400 + dep 2,640 - NWC 245 (7% x 3.5M) = 24,389. Worst (400k; CM $7.02, VC $27.98: L = 32.12 - 2.46 + 2.18 = $31.84 x 400 = 12,736). Allowed = 10,653; dividend $4.20 (= EPS, the most that counts for the price) 8,400 + retirement ~2,000 -> base **~13,990**, worst **~1,050**. Retirement size depends on the share price (UNKNOWN; cap 5% of shares) and on whether early bond retirement is allowed (UNKNOWN; VERIFY).

**Why ~$11-14M of cash remains (answering the idle-cash charge).** It is not slack. It is the cash-flow cost of a 10-15% volume miss when production is locked to the best case: $9.5M in R5, $12.5M in R4/R8. Distributions are already set to the "allowed" limit in R5-R7 (rev 2 left 0.8M and 0.7M unused). Rev 4: this cash is the Tier-1 reserve only; the Tier-2 reserve is the standing current-debt buffer X, not more idle cash. The only genuinely idle piece is the R8 buffer; in R8 re-run the test at s = 5% (seven rounds of data) and the buffer falls by ~$6M, which goes to retirement within the 5% cap. Current debt (8.6%) is repaid first; 10% bonds cannot be prepaid (UNKNOWN). That ordering minimizes negative carry.

### Tier-2 stress overlay (rev 4; lowers NI and adds the standing buffer to the pre-overlay cash above)

Extra loss T = 5% x plan units x L. Buffer X = standing current debt added on the Finance screen and rolled each Jan 1. After-tax carry = 8.6% x 0.65 = 5.6% of X (ASSUMPTION: the 8.6% rate does not rise with leverage; VERIFY). From R5 the dividend is cut by the cumulative carry (R1-R4 carry of $407K is absorbed in R5) so Tier-1 cash is unchanged.

| R | Tier-1 worst (pre-overlay) | T (5-pt extra miss) | X | Current debt total (plan + X) | Carry (after tax) | Tier-2 cash |
|---|---|---|---|---|---|---|
| 1 | 1,562 | 58.75k x 30.95 = 1,818 | 300 | 4,000 + 300 = 4,300 | 17 | 1,562 + 300 - 17 - 1,818 = **27** |
| 2 | 1,012 | 75k x 29.50 = 2,213 | 1,350 | 5,100 + 1,350 = 6,450 | 76 | 1,012 + 1,350 - 93 - 2,213 = **56** |
| 3 | 1,034 | 102.5k x 29.81 = 3,055 | 2,300 | 6,100 + 2,300 = 8,400 | 129 | 1,034 + 2,300 - 222 - 3,055 = **57** |
| 4 | 1,318 | 137.5k x 30.30 = 4,166 | 3,300 | 4,600 + 3,300 = 7,900 | 185 | 1,318 + 3,300 - 407 - 4,166 = **45** |
| 5 | 1,040 | 155k x 30.69 = 4,757 | 3,750 | 3,750 | 210 | 1,040 + 3,750 - 4,757 = **33** |
| 6 | 1,049 | 175k x 31.10 = 5,443 | 4,450 | 4,450 | 249 | 1,049 + 4,450 - 5,443 = **56** |
| 7 | 1,305 | 195k x 31.51 = 6,144 | 4,900 | 4,900 | 274 | 1,305 + 4,900 - 6,144 = **61** |
| 8 | ~1,050 | 200k x 31.84 = 6,368 | 5,350 | 5,350 | 300 | 1,050 + 5,350 - 6,368 = **32** |

Estimated limits (est.): R1 ~$9.2M (47% used), R2 ~$9.4M (69%), R3 ~$9.9M (**85%**), R4 ~$13.8M (57%); R5-R8 above $20M. NI after carry: R1 0.98, R2 4.82, R3 6.48, R4 6.55, R5 9.19, R6 9.45, R7 8.43, R8 8.10 ($M). Dividends: R5 $3.09 (6,800 - 617), R6 $2.13 (4,500 - 249), R7 $4.21 (= EPS 8,430), R8 $4.05 (= EPS 8,100) + retirement ~2,000. If the R3 limit binds, skip the gated Edge increment first (frees 3,420, which removes the need for X3), then cut the dividend. Tier-2 margins are thin by construction (they are defined as exactly 5 points); re-run them on the real proforma.

**Gating rules (apply at every save):**
- Discretionary capex (Edge increments, automation, the R7 option) is bought only if the proforma Dec 31 cash under the worst-case forecast stays >= $1.0M after the pre-funding rule. Flex order: dividend first, then automation, then Edge increments, then promo; add current debt before cutting anything else.
- **Edge increment gate (R3, +190).** Information at the R3 decision: Ease's December R2 survey score (Ease sold from ~Apr R2). Buy only if (a) the worst-case cash test passes AND (b) Ease's raw December CSS >= 0.65 x Eat's (expected launch-year k ~0.70; the raw ratio contains the awareness and age handicap of a launch year, so read it against 0.70). If (b) fails, skip (cash +3,420) and keep Edge at 260k. **The R2 Edge purchase (260k, 4,680) is NOT gated by design:** at k = 0.6 two LT products still lift share from 13.0% to 23.1% (A5 table) and the third adds ~8 points even then (~480k units at R3 demand), far above the 260k line's needs.
- **Role of PR2 (fixes a contradiction in rev 2).** PR2 measures k with the same spending and specs as CR2, but that read does NOT gate the CR2 Edge line; it is a prior for forecasting Ease's CR2 volume and for the R3 increment gate. The real December R2 score replaces it.
- **R7 capacity option (+50 Ease/+50 Edge = 1,800).** Buy only if best-case R8 production (forecast x 1.09) exceeds 4,200 (i.e. > 95% of the 4,400 ceiling) AND the worst-case test passes. One year of use: payback is thin (13.6/18), so default is NO.

**Max-investment fallback.** "Max investment" is unverified (Section 0). Estimated displayed cap at each decision = stock cap (20% x 2,000K x price; $4,468K at $11.17) + bond headroom: R2 ~9.2M, R3 ~10.2M, R4 ~11.5M (all >= planned capex 4.7M / 5.9M / 2.3M). If it counts only bond headroom (stock never issued): R2 4.7M >= 4.68M (just), R3 5.7M vs 5.94M (short by 258K), R4 7.1M >= 2.3M. Fallback if PR1 shows the cap binds on cash-funded capex: (a) in R3 trim the Edge increment from +190 to +175 (3,150, total 5,670), then defer the rest; (b) issue only the missing stock (5% fee: raising $0.3M costs $15K) if the price is then above $11; (c) never fund a plant shortfall with the emergency loan. PR1 tests the cap directly (Section D, Finance step).

### C2. Stage 2 (gated): a High Tech product "Echo", re-costed over R5-R8

**Why it is back on the table.** Rev 2 priced HT as a single R3 snapshot. HT demand grows 20%/yr (R5 5,375k, R6 6,450k, R7 7,740k, R8 9,287k), the late LT lines now earn only 0.25, and cash otherwise piles up. All Echo inputs below are ASSUMPTIONS (the brief gives no HT cost data beyond positioning-cost anchors).

| Input | Value | Basis |
|---|---|---|
| Spec | 10.5/9.5, MTBF 21,000 (HT range 17,000-23,000) | Inside 2.5 of the HT ideal for all of R5 (R4-end ideal 10.2/9.8, R5-end 10.9/9.1); needs a yearly ~0.7 reposition from R6 |
| R&D | Start Jan 1 R3; ~$1M/yr (ASSUMPTION: 27 months, revision Apr 1 R5; a far move from existing products, so it may take longer, brief range 3 months to 3 years; PR1 probe reads the real date) | brief: $1M per project-year, 3 months to 3 years |
| Line | 700 @auto 3 bought R4 (12,600), +100 R5 (1,800), +50 R6 (900) = 850 | auto <= 4 for HT (brief guidance) |
| Price / material | $40 (HT price score ~20); material $21.0, 22.0, 23.0, 24.0 for R5-R8 (leading-edge positioning ~$10 + MTBF $6.3 + base $4.5; ASSUMPTION +$1/yr) | brief anchors |
| Units (share of HT) | **525 (launch ramp: 9 months x 700/12; 800 only if revision by Jan 1 R5)**, 1,100 (17%), 1,350 (17.4%), 1,550 (16.7%) | ASSUMPTION k = 0.7-0.85, r = 4 HT rivals |
| CM per unit (labor formula) | $10.0, 7.8, 6.4, 5.0 (m = 0%, 27%, 37%, 45%) | single labor formula |

| Year | CM $M | Promo+sales $3.0M | R&D | Dep | Interest (7.0M bonds + ~4.5M current debt) | Pre-tax | After-tax NI |
|---|---|---|---|---|---|---|---|
| R3 | - | - | -1.0 | - | - | -1.0 | -0.65 |
| R4 | - | - | -1.0 | - | -1.0 | -2.0 | -1.3 |
| R5 | 5.3 | -3.0 | -1.0 | -0.84 | -1.0 | -0.5 | -0.35 |
| R6 | 8.6 | -3.0 | -1.0 | -0.96 | -1.0 | +2.6 | +1.7 |
| R7 | 8.6 | -3.0 | -1.0 | -1.02 | -1.0 | +2.6 | +1.7 |
| R8 | 7.8 | -3.0 | 0 | -1.02 | -1.0 | +2.8 | +1.8 |

**Launch-year sensitivity (700 line, CM ~$10, pre-tax):** revision Jan 1 R5 = 700k first shift (+2nd shift, VERIFY) ~$7.6M; Apr 1 = 525k = $5.3M (base); Jul 1 = 350k = $3.5M (R5 pre-tax -2.3M); Oct 1 = 175k = $1.8M. Cumulative NI +$2.9M (was +$4.4M); R8 EPS +$0.9 (4.05 -> ~4.95); R8 total share (4,000 + 1,550)/20,091 = **27.6%** vs 19.9%. Return before marketing 0.60 per $ per year, after marketing 0.18-0.25: positive but not great, so it is a share-and-EPS play, not a margin play. R4 funding (both tiers, rev 4): line 12,600 less bonds 7,000 (net 6,650); no R4 dividend or repayment; R4 pre-surplus Tier-1 cash 3,818 - 12,600 + 6,650 + current debt 4,500 = 2,368 (>= 1,000), but Tier 2 = 2,368 - 4,166 = -1,798, so current debt must be ~12,400 total (6,100 rolled + 4,500 + 1,800), 90% of the est. $13.8M limit. If the Finance screen limit is below that, or bond headroom is below 7,000 (est. 7,052, only 52 spare), issue stock for the gap (5% fee; max $4,468K x 0.95) or cut the line to 650 (-900). Echo has no R4 sales, so the loss terms are unchanged. R5-R6 dividends fall to ~$0.30 and ~$1.00 while the current debt is repaid; dividends resume in R7 (stock price uses the last TWO years of dividends, a real cost). Figures are approximate; recompute on the R4 proforma.

**Gates (all four):** (1) PR1 probe shows a new-product revision at 10.5/9.5 within 27 months of Jan 1 (Apr 1 R5, the base case; every month later = 58k fewer R5 units, ~$0.6M CM); (2) Ease's observed k (Dec R2) >= 0.65, proving a new product can launch cleanly; (3) the R4 proforma passes BOTH cash tiers with the funding above; (4) HT growth published in FastTrack >= 15%/yr and fewer than 2 rivals hold two HT products. If any fails, do not buy the line; the cash goes to dividends and the R3-R4 R&D (~$2M) is the sunk cost. Check gate (1) in R3 before spending R&D: if the PR1 probe shows > 27 months, do not start.

### R1 and R2 notes (what each choice rests on)

- **Eat 5.3/14.7, MTBF 20,000** (book: Nov 9, material ~$12.00, age 2.0 on Nov 9, ~2.1 at year-end). If the R&D screen shows a date after Dec 1 (because Ease runs at the same time), fall back to 5.4/14.6 (Sep 25, $744K, $12.54). R1 saving with the Nov 9 version is small ($3.97 x 14% of the year x 1,175k = ~$0.65M) but R2 onward gets the full $4.8M/yr.
- **Ease 5.5/14.5, MTBF 20,000:** near Eat, so the project is faster; it stays within 2.5 of the LT center until the center passes ~7.27/12.73 (about R5). Material ~$12.9 (interpolated from the book's 5.4/14.6 -> $12.54).
- **Price $35** (LT ceiling). Eat's HT buyers still see $35 inside the HT range (HT price attractiveness ~40).
- **A/R 30 days throughout R1-R8.** The CSS gain of 60-day terms is (1 - 0.007)/(1 - 0.07) = +6.8%. R3: share 38.2% -> 39.7%, +86k units x $11.8 = +$1.0M, against interest on 5.9M of extra A/R at 8.6% = $0.5M; R5: +121k x ~$10 = $1.2M vs interest on $8.9M = $0.77M. A thin +$0.3-0.5M after tax that parks $6-9M of cash, which the worst-case test cannot spare before R7. Treat 60 days as an R7-R8 option only if PR data show the CSS effect and the test still passes.
- **No stock issue.** Stock costs 5% fees plus dilution; bonds at 10% with a 5% fee are cheaper per dollar of capacity.

---

## D. Practice Round 1: exact decisions, screen by screen

**Deadline: PR1 ends 10/11/26 11:30 PM, timezone UNCONFIRMED. Today is 10/10, so finish and save by about 6 PM on 10/11. Confirm the timezone with the instructor.**

**R&D**
- Eat: Pfmn 5.3, Size 14.7, MTBF 20,000. Expect revision ~Nov 9, material ~$12.00, R&D ~$0.86M. VERIFY each.
- New product "Ease": Pfmn 5.5, Size 14.5, MTBF 20,000. VERIFY revision date and cost (expect >= 12 months, roughly $1M+). Record how the date moves with both projects vs alone.
- **Probe (do not save):** on a scratch third new product enter 10.5/9.5, MTBF 21,000 and read the revision date and cost (gate 1 of Stage 2), then delete the entry.

**Marketing**
- Eat: price **$35**, promo **$1,500K**, sales budget **$2,000K**, A/R **30 days**, Your Forecast **min(1,175, 0.95 x the benchmark prediction read on this screen at the final price/promo/sales settings)** (1,175 = 850 LT + 325 HT, ASSUMPTION; corrected-accessibility model gives ~1,230 so 1,175 is already ~5% under it).
- Ease: nothing yet (VERIFY the screen allows blank).

**Production**
- Eat: forecast 1,175 -> available = 1,175 + 1,175/11 = 1,282; minus inventory 87 = 1,195; divide by 0.99 -> **schedule 1,207**. Capacity buy 0; automation 3.
- Ease: **capacity buy 380, automation 3** (380 x $18 = $6,840K <= $6,948K). Schedule 0.
- A/P 30 days.

**HR:** defaults (complement 250, wage $20, benefits $2,500, profit sharing 2%, recruiting $0, training 0). PR1 is the HR baseline; the levers are tested one per round in PR2-PR5.

**Finance:** bonds **$2,480K**; current debt **$4,300K** ($4,000K Tier-1 pre-funding + $300K Tier-2 buffer); stock issue 0; retire 0; dividends **$0**.
- **Max-investment test (before the final values):** temporarily enter Ease capacity 450 (cost $8,100K > the $6,948K cap) and see whether the screen blocks it, warns, or lets it through with only bonds + cash. Record the result, then restore 380.

**Pre-save checks (all four must pass):**
1. Revision dates: Eat <= Dec 1 (target Nov 9); Ease date shown.
2. CM: Eat blended CM >= 24% at $35 (model says 26%).
3. Dec 31 cash under TWO worst-case forecasts, production fixed at the best case: Tier 1 (set 1,000, s = 15%) >= $1,000K (model ~$1,845K with $4.3M current debt); Tier 2 (set 940, s = 20%) >= $0 (model ~$27K). If either fails, raise current debt by the shortfall (limit ~$9.2M, VERIFY). Then restore the forecast and keep production from the best case.
4. Ending inventory: >= 1 unit and <= 1/6 of available (1,282/6 = 214k). Plan gives 107k (8%) at 1,175 sales; ~282k (22%) in the 1,000 worst case, which breaches 1/6 and is acceptable as a test, not as a plan.

**Experiments to run BEFORE saving (benchmark prediction on Marketing):** one variable at a time, record predicted units and revenue: price $30 / $35 / $40; promo $1.0M / $1.5M / $3.0M (this calibrates ASSUMPTION 9, the $1.0M point); sales budget $1M / $2M / $3M; A/R 30 / 60 / 90 days; MTBF 17,000 / 20,000 (on R&D, material cost vs benchmark). Then reset to the values above and save once.

### What PR1-PR5 should test (practice runs the same industry for 5 years, then resets; rules carry over, state does not)

| Round | Tests |
|---|---|
| PR1 (2027) | Revision dates and costs with 1 vs 2 projects. **Max-investment behaviour.** Benchmark sensitivities above, incl. the promo curve below $1.5M. HT-ideal new-product R&D probe. Whether Eat keeps HT sales after repositioning. **Accessibility decay: confirm 40% -> ~49% with $2M (and the g(budget) points in fact 7).** **HR baseline** (defaults) and where the HR/BSC L&G numbers appear. |
| PR2 (2028) | **Clean k measurement only:** Ease promo $1.0M, Eat $1.5M, same price $35, same specs, read both December scores; k = Ease CSS / Eat CSS (prior 0.70, R3 gate 0.65). Ease actual launch date and monthly ramp (<= 1/12 capacity per month; does the 2nd shift lift it?). Classify each rival. Does the forecast-vs-actual miss stay within the s values in C? **HR test 1: wage $20 -> $22 for this round only**; record unit labor cost, any productivity/turnover or BSC L&G reading, and NI. No price or A/R changes in this round. |
| PR3 (2029) | Accessibility with 3 products in the LT fine cut (does it hit ~100%?). **Price A/B (separate from k):** Ease at $32 vs Eat at $35 (compare CSS ratio to the +8% model). A/R 60-day effect. Automation 3 -> 4 on Eat: cost, whether labor saving is immediate, R&D date lengthening (gate for the Eat option). Age curve (Eat at 4.1 vs 2.x). One deliberate $38 price on a single product (above-range penalty). Repeat the k read for Edge. **HR test 2: training 0 -> 20 hrs.** |
| PR4 (2030) | Rehearse CR4 end to end including the bond maturity cash call. Seller's market test: compute the Branch S ratio from the FastTrack and try the ladder on one product ($36/$37/$38; also one at $40), recording units sold and year-end inventory. Stagger repositioning (two simultaneous projects vs one). Small stock issue (fee and price effect). **HR test 3: profit sharing 2% -> 4%.** Stage 2 rehearsal: read an HT product's CSS/share if a rival has one. |
| PR5 (2031) | Endgame cash: dividends vs EPS, stock retirement, current-debt payoff, early bond retirement if allowed, effect on stock price. Dry-run the save protocol and clock. **HR test 4: recruiting spend $0 -> a modest figure.** HR decision rule: adopt a lever in the competition only if its measured benefit (productivity/L&G reading, or unit cost) exceeds its cost; otherwise keep defaults. |

---

## E. Decision rules for adapting each round (read the new FastTrack first)

**Read in order:** (1) segment demand and next year's published growth rates; (2) December survey scores by product and segment (compute k = new product CSS / Eat CSS); (3) perceptual map; (4) market share actual vs potential, plus stock-outs; (5) each rival's capacity, automation, products and prices; (6) our CM, utilization, cash and upcoming bond maturity (R2, R4, R6).

| If you see | Do |
|---|---|
| A rival cuts LT price to $25-$30 | Hold $35 (B marginal test: ~$0.4M gain vs ~$2.05M cost per $1). Re-test only if our share falls below 80% of plan for two rounds; then try a $2 cut on ONE product and compare CSS. |
| Rivals pile into HT with repositioned Eat | Stay LT, raise accessibility, expect LT share per product to rise. Do not chase; Stage 2 gate (4) counts rivals with two HT products. |
| Actual share < potential share (stock-outs) | Next year available = F + F/11, use the 2nd shift; use "potential" share in the forecast. |
| Seller's ratio (rivals' + our 2 x first-shift capacity, over next-year demand) < 1.00 | Branch S ladder in C: +$1 at 0.90-1.00, +$2 at 0.75-0.90, +$3 below 0.75, max +$4 until PR4 data; all three LT products; step back $1 if year-end inventory > 1/6; re-run both cash tiers at the new price. |
| A rival buys big capacity | Check its price; expect a price war next round. Do not add capacity beyond the capacity rule. |
| Rival launches a second LT product | Add promo to defend awareness; make sure Edge is on schedule. |
| Ease raw CSS < 0.65 x Eat's in December R2 | Skip the Edge increment AND Stage 2; put cash into dividends and retirement. |
| Revision date of Ease/Edge later than assumed (Apr 1) | Cut that round's forecast by the missed months x 1/12 of line capacity and re-run worst-case cash before saving (Jul 1 = -$1.1M, Oct 1 = -$2.3M). |
| Next-year production for ONE LINE > 1.85x that line's first-shift capacity (per line, not pooled) | Buy first-shift increments for that line (capacity rule, per-product table in C). If it is <= 1.85x, do NOT buy: the 2nd shift is cheaper. |
| Actual forecast miss exceeds the s used in C two rounds running | Raise s by 5 points in the worst-case test and pre-fund with current debt; cut dividends first. |
| HT growth is raised above 20% or LT growth falls | Pull Stage 2 forward only if R4+ worst-case cash after capex is >= $6M; it must be new, near the HT ideal, automation <= 4. |
| Tier-1 worst-case Dec 31 cash < $1.0M, or Tier-2 (+5 pts) < $0 | Pre-fund with current debt; if the limit binds, skip the gated Edge increment first, then cut dividend, automation, promo. |
| CM < 28% | Branch S price if the ratio allows; otherwise defer a reposition; do not cut price. The MTBF trim is NOT a profit lever (break-even, see B2); use it only to hit a BSC CM target. |
| A product is > 2.1 from the LT center at next year-end, or age > 4.5 | Reposition it this round (table in C shows the planned moves). |
| Our LT share > 45% and capacity is full | Stop adding lines; shift cash to dividends and retirement. |

---

## F. Top risks and prevention

| Risk | Why it matters | Prevention |
|---|---|---|
| Stock-out | Customers go to the next choice | Stock = F + F/11 (60-day cap); watch the 1/6 rule. |
| 2nd-shift ceiling | By R8 production is 91% of 2 x first shift | Capacity rule, R7 option gate; re-check best-case production against 2x first shift every save. |
| Emergency loan | Negative Dec 31 cash -> current rate + 7.5% and stock price hit | One worst-case formula (C) every round, two tiers (s and s + 5 pts); the base plan passes both in all eight rounds; pre-fund with current debt; count the R2/R4/R6 bond maturities; the tail beyond Tier 2 costs ~16.1% on the shortfall (priced in C). |
| Max-investment cap binds | Capacity wall unfunded | Fallback in C; PR1 test. |
| New product late or weak (k < 0.65) | Idle line, lower volumes | Apr 1 launch assumption with late-revision sensitivity; Edge increment gated on Ease's observed R2 score; adjust forecast by actual revision date. |
| R&D overrun | Reposition slips past Dec 31, or a product leaves the fine cut | Reposition table in C; check dates on the R&D screen; fall back to a shorter move; avoid automation > 5 on LT lines. |
| Price war | Rivals cut price | Do not follow (B); retain MTBF/accessibility advantage. |
| Cost drift | Material rises ~$5 by R8, CM -> 20% | MTBF trim, reposition only the minimum, no wage raises beyond defaults; BSC cost accepted knowingly. |
| Overcapacity | 2,200k first shift in R7-R8 is justified only at >= ~35% LT share | Stop buying when share < plan for two rounds. |
| Credit squeeze | Current debt up to $8.4M in R3 (85% of est. limit; ~$12.4M in R4 with Stage 2) raises leverage | Repay from R4; do not exceed the limit; leverage is a BSC cost, accepted knowingly. |
| Model optimism (NI gap, k, material path) | Cash plan too rosy | Plan only from proformas; worst-case volume haircut every round; sensitivity tables in A5 and C. |
| Save overwrite (5 people) | Last save wins | Section G protocol. |

---

## G. One-page summary, owners and save protocol

**Strategy:** Niche Cost Leader in Low Tech. Three LT products (Eat now, Ease from ~Apr R2, Edge from ~Apr R3), priced $35 (the LT ceiling), MTBF at the range top (20,000), positioned on the cheap trailing edge of the LT drift path and re-moved on the dated schedule in C. Capacity: Ease and Edge lines bought a year ahead, increments only when production would exceed 1.85x first shift; Eat never expanded. Funding: bonds + current debt (with a pre-funded cushion), no stock issue. Cash returned R4-R8 (current-debt payoff, dividends up to EPS, retirement). Stage 2 (HT product Echo) only through its four gates.

**Targets:** R1 Eat repositioned by ~Nov 9, CM >= 24%, worst-case cash >= $1.0M. R3: three products, ~31% LT share, CM 34%, NI ~$6.5M. R5: 3,100k units, CM 28%, NI ~$9.2M. R8: ~4,000k units, ~37% LT share, 19.9% total share (27.6% with Stage 2), CM ~20% (higher with Branch S), EPS ~$4.05 (~$4.95 with Stage 2).

**Five rules:**
1. Price $35; never follow a price cut without the E test.
2. MTBF at the top of the range; promo $1.5M per product ($1.0M in a launch year); sales budget $3-$4M shared.
3. Buy capacity a year ahead only when production would exceed 1.85x first shift; run the two-tier worst-case formula (with bond maturities) before every save and pre-fund with current debt; apply Branch S pricing when the seller's ratio says so.
4. Reposition on the dated schedule; keep every product within ~2.1 of the LT center.
5. Plan from proformas, not from this document's model.

**Owners (5 members):**

| Member | Department | Owns |
|---|---|---|
| 1 | R&D + Production | Positions, revision dates, schedule, inventory rule, capacity and automation, the 1.85x rule |
| 2 | Marketing | Price, promo, sales budget, A/R terms, forecast |
| 3 | Finance | Bonds, current debt, dividends, worst-case cash check, bond-maturity calendar, emergency-loan watch |
| 4 | HR + competitor analyst | HR tests PR2-PR5 and HR decision rule, FastTrack rival tracker, Section E triggers, k measurement |
| 5 | Captain / integrator | Resolves conflicts, runs pre-save checklist, the only person who saves |

**Save protocol:**
1. Each owner writes proposed numbers in the team sheet by T-24h; the captain freezes them at T-6h.
2. Only the captain saves, via File > Update Official Decisions, once.
3. After saving, a second member re-opens each screen and ticks the pre-save checks against the sheet.
4. Nobody else touches the sim after the freeze. Screenshot each screen.
5. Check the deadline timezone with the instructor; never plan to save inside the last hour.

---

## H. VERIFY list before trusting any number

1. Material cost at 5.3/14.7, 5.5/14.5, 5.9/14.1 and the MTBF effect (book $16.04 vs your screen $15.97), and the blended material path to $17 by R8.
2. Revision dates for one vs two simultaneous projects; Ease/Edge launch dates (assumed Apr 1); HT-ideal probe date.
3. Whether capex can exceed "max investment" using cash, and whether capacity can be added to an existing line.
4. Tax rate, SG&A, interest on old bonds (model gap ~$0.5M/yr, already deducted); annual wage raise (assumed 0).
5. How automation changes affect R&D time and when savings begin.
6. LT age curve above 3.1 and for age 0-2 (determines k); promo response between $1.0M and $1.5M.
7. Bond maturities treated as cash repayments in R2, R4, R6; whether rolling or early retirement is allowed.
8. Which rivals buy capacity (seller's market test).
9. The current-debt limit on the Finance screen (the plan uses up to $8.4M in R3 incl. the Tier-2 buffer, ~$12.4M in R4 with Stage 2).
10. The deadline timezone.
11. Whether the 2nd shift is limited to the line's first-shift capacity during a launch ramp.
12. What the HR screen levers do (PR2-PR5 tests).
