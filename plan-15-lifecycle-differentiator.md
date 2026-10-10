# Team Erie - Capsim Foundation strategy (Industry F165279) - REVISED (round 3)

Round-3 changes: current debt capped by the brief's limit formula using the plan's own A/R and prior-year labor+material (A10); full-year interest on every new bond and on all current debt (10% bonds, 8.6% current debt, existing bonds assumed 10%); the 2030 ($1,733K, R4) and 2032 ($2,600K, R6) bond maturities, which earlier rounds omitted, are now in the cash tables; a third stock tranche; dividends resized from the corrected worst cases; the Edge share claim re-tested under a common CSS scale error; Edge position/material trade-off priced; stock-price claim removed. Cash tables were rebuilt with one consistent model (section C header).

**One-line verdict.** Run a *Differentiator with Product Lifecycle Focus*: (1) turn Eat into a cheap LT cash cow in R1 (about $4/unit cheaper material, worth about $3.4M/yr at Eat's real volume); (2) start a NEW young HT product ("Edge") in R1 and buy its capacity in R1, gated on the revision date the R&D screen actually shows; (3) scale Edge's capacity ahead of HT growth (HT grows from 32% of demand to 46%), every purchase from R4 capped by Edge's measured share; (4) keep Eat in the LT fine cut with two cheap book-point repositions (R4, R6); (5) pay out cash R5-R8 only as far as the worst-case test allows (no dividend in R1-R4). Edge is a bet that HT share stays at about 28-30% or more; section B says what happens if it does not.

## 0. Conventions and assumptions

Everything uses only the brief. Anything not in the brief is tagged ASSUMPTION (A#) or NOT IN DATA.

- A1. CSS model (not stated in the rules): CSS = sum(weight x criterion score) x (1+awareness)/2 x (1+accessibility)/2. It does NOT reconcile with the Dec scores. For Eat in LT, even with a ~0 price score, it gives 0.29x96 + 0.21x100 = 48.8 raw, times 0.775 x 0.70 = 26.5, against the actual 18. **Use it for direction only. Every price number below is a starting point that PR1-PR3 must overwrite with measured elasticity.**
- A2. Segment growth stays at 10% (LT) and 20% (HT). FastTrack publishes changes.
- A3. The default R1 dividend is $1,000K (the R0 value). Verify on the Finance screen.
- A4. Tax rate 35%. Not in the brief. Used only to turn pre-tax profit into cash after R1. R1 cash starts from the screen's own $4,470K and ignores the small tax change from my edits (covered by the buffer).
- A5. New-product R&D time. PROXY ONLY. The brief gives R&D time for Eat moves, not for a new product, and says a new product's invention takes >= 1 year; the new product's start point and distance are NOT IN DATA. Fit of the book's Eat points (distance d -> months from Jan 1): 0.71 -> 4.1; 1.41 -> 8.8; 1.56 -> 10.3; 2.40 -> 15.6; the smallest move 0.14 -> 1.5 sits above the line (a floor). For d >= 0.7: months ~ 6.7 x d - 0.6 (errors <= 0.5 month on the four points). I use it for repositions of an existing product (Edge after launch: d = 0.99 -> 6.0 months, about Jul 1; cost about $1M per project-year). For Edge's FIRST launch I use Apr 19 R2 only as an illustration; the plan's base case and every gate use the date the R&D screen shows (A17).
- A6. Edge material cost, extrapolated from book points ($17.24 at 7.4/12.6): about $19.5 at MTBF 20,000, plus $0.90 for MTBF 23,000, about $20.4. VERIFY.
- A7. Labor at automation 3, first shift: $11.20 - 2x$1.12 = $8.96; second shift x1.5 = $13.44 (so first-shift unit cost = material + 8.96, second-shift = material + 13.44). Annual raise NOT IN DATA.
- A8. The fine cut is measured from the ideal spot (for HT, from the ideal, not the center). The brief says "segment center". VERIFY on the perceptual map.
- A9. "Max investment" $6,948K is about projected year-end cash + max bond ($4,470K + $2,480K = $6,950K). Max bond $2,480K = 80% x net fixed assets $9,600K - existing bonds $5,200K (exact). Max stock $4,468K = 20% x 2,000K x $11.17 (exact). VERIFY that these update when I change other decisions.
- A10. (corrected round 3) Current debt limit by the brief's formula: (0.75 x A/R + 0.15 x last year's direct labor + material) x 1.2. At 30-day terms A/R = revenue/12 (Eat's R0 A/R $3,353K on $40.8M sales confirms 30 days = 8.2% of sales). R0 data: (0.75 x 3,353 + 0.15 x (1,200 x 26.57 = 31,884)) x 1.2 = about $8.76M. This plan's own path: R2 limit uses R1 (revenue $39.0M, A/R $3.25M; labor+material about $32.5M): about $8.8M. R3 uses R2 (revenue $40.9M, A/R $3.41M; labor+material 19.3 + 10.4 = $29.7M): (2.56 + 4.46) x 1.2 = about $8.4M (the earlier $10.9M used an A/R of $6.3M that the plan's own R2 revenue cannot produce). R4 uses R3 (revenue $76.9M, A/R $6.4M; labor+material about $56M): about $15.9M. R5 about $19.8M. Rule used in this plan: never plan a balance above 90% of the estimate, and read the live Finance screen, which is the authority. R2/R3 balance is $7,500K (89% of $8.4M).
- A11. Practice-round rivals are the same six teams and are readable in FastTrack. Rival HT CSS about 16 each: this is Eat's own December HT score in the brief, i.e. what an untouched default product earns. It holds only for rivals that leave HT defaults alone. A rival that moves Eat to the LT ideal 5.3/14.7 is 3.96 from the R1 HT ideal (outside the 2.5 fine cut) and scores below 16 in HT, which RAISES Edge's share; so 36% is not optimistic on that count. The risk is a rival that builds a young HT product (section E), and the A1 level error, addressed by the share-ceiling rule below.
- A12. Sales for R1: base case 1,220 units for cash math (between benchmark 1,122 and equal-share 1,356); production forecast F = 1,250 (section D).
- A13. Other fixed costs (admin etc.) about $0.85M/yr from the R0 plug. Rough.
- A14. (new) Multi-project allowance. R1 runs Eat and Edge projects together. I price Eat's project at $1,000K (vs $860K single) and keep Edge's R1 charge at $1,000K. Dates may slip; the decision tree in section D handles it. Capacity additions to an existing line in increments are assumed allowed; NOT IN DATA, verify on the Production screen (each product has its own line; the site holds up to 4 more lines).
- A15. (new) Material cost of Edge rises with each reposition: book points imply about $0.80 per 0.5 Pfmn, so about +$1.12 per 0.7 step, applied from the revision date. Average over the year: R3 +0.56, R4 +1.68, R5 +2.80, R6 +3.92, R7 +5.04, R8 +6.16 (if repositioned every year; section C skips R8).
- A16. (new) Eat material path (book points, MTBF 20,000): 5.3/14.7 about $12.00 (after the Nov 9 R1 revision); 5.9/14.1 $14.54; 6.9/13.1 $16.44. Moving Eat toward the leading edge RAISES material: Eat's R1 saving of $3.97/unit shrinks to $1.43 at 5.9/14.1 and to -$0.47 at 6.9/13.1 (vs $15.97 start; vs $12.00 it costs +$2.54 and +$4.44). This is why Eat is moved only when the fine cut forces it (section C).
- A17. (new) Edge launch date. The R2 base case assumes a Jul 1 R2 revision = the gate threshold (section D tree), NOT a forecast. The line purchase is made only if the R&D screen shows <= Jul 1.
- A18. (new) The "-18% worst case" is an ASSUMPTION, not a brief number. Source: R1 only: 1,000 units (a pessimistic round figure) vs the 1,220 base is -18%; the same percentage is then applied to revenue in every later round as a stress (cash effect = 18% x revenue x 11/12, production fixed at the best case, no tax shield, no inventory resale: deliberately harsh). Replace it by a measured rule once data exist: worst-case shock s = max(10%, 2 x the largest forecast miss seen in PR1-PR5 and completed rounds). Until PR2 data exist, use 18%. Base cash minus worst-case cash IS the shock, so the large base balances in section C are the required buffer, not idle money; every dividend and repayment below is shock-limited, and the release rule is: extra payout available in a round = (0.18 - s) x revenue x 11/12 (e.g. s = 10% frees about $9M in R6 and $12M in R8).
- A19. (new, round 3) Existing bonds are assumed to carry 10% (their coupons are NOT IN DATA); the maturities in the brief ($867K 2028 = R2, $1,733K 2030 = R4, $2,600K 2032 = R6) are repaid in the maturity round. New bonds and new/rolled current debt are charged a full year of interest in the year raised (decisions made at the year start). Tax 35% on positive pre-tax (A4).
- A20. (new, round 3) Stock issued at the screen price of $11.17 (the max-stock figure on the screen implies the issue price is the current price, so a R1 dividend change should not alter the R1 issue price; VERIFY on the Finance screen after editing the dividend). Later issue prices are NOT IN DATA; $11.17 is used for cash math only.

## A. Diagnosis: the facts that decide this market

1. **The two segments need different games.** LT weights: price 41, age 29, MTBF 21, position 9. HT: position 33, age 29, price 25, MTBF 13. LT is a price/cost game; HT is a position and youth game.
2. **Demand (A2), thousand units:**

| Round | LT | HT | Total | HT share | Total / 9,600 industry max |
|---|---|---|---|---|---|
| R1 | 5,544 | 2,592 | 8,136 | 32% | 85% |
| R2 | 6,098 | 3,110 | 9,208 | 34% | 96% |
| R3 | 6,708 | 3,733 | 10,441 | 36% | 109% |
| R4 | 7,379 | 4,479 | 11,858 | 38% | |
| R5 | 8,117 | 5,375 | 13,492 | 40% | |
| R6 | 8,929 | 6,450 | 15,379 | 42% | |
| R7 | 9,822 | 7,740 | 17,562 | 44% | |
| R8 | 10,804 | 9,288 | 20,092 | 46% | |

   - Industry maximum with all second shifts is 6 x 1,600 = 9,600. The seller's-market threshold is R3 unless rivals add capacity. Rivals must add lines a year ahead; whoever holds spare capacity in R3+ sells at above-range prices.
3. **Repositioning Eat to the LT trailing edge is the best-value move in the sim.**
   - Material falls from $15.97 to about $12.00 (book plan 5.3/14.7, MTBF 20,000): about $3.97/unit.
   - Real volume: Eat's line is 800 first-shift units (about 850-900 with a little second shift), so the saving is about $3.97 x 850 = **$3.4M/yr**, not $5.2M. R1 gets only about 1.7 months (Nov 9 on) of it, about $0.6M. First full year is R2.
   - Cost: about $0.86M of R&D single-project (A14: $1.0M used).
4. **Eat's position is mostly irrelevant for LT score, but the fine cut is not.** Position is 9% of LT. Eat at 5.3/14.7 (after the R1 move) sits at distance from the LT center (year-end): R1 0.00, R2 0.71, R3 1.41, R4 2.12, R5 2.83 (outside the 2.5 fine cut; outside costs -1% just outside to -50% halfway to the rough-cut edge on the WHOLE score). So Eat needs a reposition in R4 and again in R6 (section C, A16) even though each one gives back part of the $3.97 saving. The real LT levers remain price and age (LT age ideal 3.0, so age 2-3 is fine).
5. **For HT the book shows one product cannot be both well positioned and young.** Eat to HT 8.1/11.9 = revision about Apr 19 NEXT year, year-end age about 2.9 (HT age score about 30; about 85 at 0.5). The gap is about 55 x 0.29 = 16 raw points (about 20% of CSS). So the HT product must be NEW.
6. **Financing envelope in R1 (A9, A10).** Bonds $2,480K x 0.95 = $2,356K; stock up to $4,468K x 0.95; current debt up to about $8.76M. Existing bonds: $867K due 2028 (R2), $1,733K 2030, $2,600K 2032.
7. **Cheap CSS lever: A/R terms.** 60 days costs 0.7% of CSS against 7% at 30 days (6.3-point gain) for about one extra month of sales in A/R at 8.6%. Too cash-hungry while the worst case is thin (R1-R4: worst-case cash is under $3.1M). Revisit from R5.
8. **Edge's margin is squeezed by its own repositioning (new).** HT must move every year, material rises about $1.12 per step (A15) while HT price is capped near $45 (each $1 above costs about 10% of price score). Edge first-shift CM falls from about 30% at launch to about 22% by R7. The instructor's 30% target cannot be held; blended CM goes 27% -> about 25% (R4) -> 17% (R7) -> 15% (R8) (section C), also because Eat's material rises with its two repositions (A16). This is the main structural cost of the strategy and it also hits any HT rival.
9. **What 5 identical rivals will probably do (ASSUMPTION; no rival data).** Most likely they copy the book plan (Eat to LT ideal 5.3/14.7, MTBF 20,000, no HT product); some leave defaults; one or two overspend on promo or capacity. Result: LT is a 5-6 way commodity fight with falling prices; HT is empty because their Eat at 5.3/14.7 is 3.96 from the R1 HT ideal. Exploit: do not chase LT price; own HT with a purpose-built product; hold capacity into R3. If two or more rivals field a young HT product in the HT fine cut, the Edge share assumption fails (section B bear case, section E).

## B. Strategy choice

**Chosen: Differentiator with Product Lifecycle Focus, broad form.** Eat = LT cost-leading cash cow. Edge = new HT differentiator launched young. An Edge II option exists from R5 if cash and rival behavior allow.

### Numbers against two alternatives (R3 plan case)

| | C: Niche Cost Leader (LT only) | B: Niche Differentiator (move Eat to HT, no new line) | A: chosen (Eat LT + new Edge HT) |
|---|---|---|---|
| Capex R1-R2 | 0 | 0 | $5.94M + $5.4M = $11.3M |
| Capacity | 800 (+2nd shift) | 800 (+2nd shift) | Eat 800 + Edge 630 |
| Unit cost, first shift | Eat $21.0 | about $29-30 | Eat $21.0; Edge about $29.4 |
| Price | $28-31 | $42 | Eat $30; Edge $43 |
| R3 CM | about $7M | about $13.5M (1,160 units, 27%) | about $20.6M (26.8%) |
| R3 pre-tax profit | about $2M | about $7.8M | about $10.0M (after about $2.1M interest and $1.7M depreciation; was $10.5M before the round-3 interest correction) |
| Main weakness | Crowded segment; price-war exposure; LT falls from 70% to 54% of demand | Age handicap; capped at 1,600 units; single point of failure | Capex committed before the R&D date is certain; share-dependent |

- B math: HT share about 31%. Raw CSS ~54 x 0.67 = 36 vs rivals 5 x 16 = 80 gives 36/(36+80) = 31% x 3,733 = 1,160 units. CM = (42 - 30.4) x 1,160 = $13.5M. B's pre-tax figure is its own estimate, with fewer fixed costs than A.
- A math: Edge raw about 69 x 0.67 = 46 gives 46/(46+80) = 36.5% x 3,733 = about 1,360 units; plan uses 1,230 (630 first + 600 second) in R3 because capacity binds.
- **Payback, with interest.** A's pre-tax lead over B at R3 is 10.0 - 7.8 = about $2.2M (A's figure carries its interest and depreciation). Extra capital in A through R3 is about $11.3M capex + $1.7M of extra R&D = $13M, after-tax lead about $1.4M/yr at R3: payback is slow if R3 were the steady state. It is not: B's HT output is capped at 800+800 = 1,600 units (and it gives up LT), while HT demand reaches 5,375 by R5. Approximate A-minus-B pre-tax gap: R3 2.2, R4 about 3, R5 about 4.5, R6-R8 about 5.5 each (B capped around $10.6M pre-tax = 1,600 units x $11 less $7M fixed; A from section C, after the round-3 interest correction). Cumulative about $26M pre-tax over R3-R8 against about $24M of A capex through R4 (undiscounted; recovering 65% of capacity cost if sold is NOT counted). So A wins on the horizon, but the margin is thin; the case for A is B's 1,600-unit cap plus the share gates below, not a large NPV.
- **Common CSS-scale error (round 3).** A1 overstates Eat's LT score (26.5 modelled vs 18 actual, ratio k = 0.68). Applying k to Edge (46 -> 31) against the actual rival HT score of 16 each (5 x 16 = 80) gives 31/(31+80) = 28%. But A1 is also the source of B's 36, so k hits B too: 36 x 0.68 = 24.5, 24.5/(24.5+80) = 23%. Under k both fall; the ratio A:B stays about 1.2. R3 with k: A: Edge 28% x 3,733 = 1,045 units (630 first at 29.92 + 415 second at 34.40 = $33.1M cost vs $44.9M revenue, CM $11.8M) + Eat $7.2M = $19.0M CM, less fixed 8.43 + interest 2.13 = pre-tax about $8.4M. B: 23% x 3,733 = 859 units x ($42 - 30.4) = $10.0M CM less $5.7M fixed = about $4.3M. A still leads by about $4M, and Edge's 630 first-shift capacity (needs only 0.7 x 1,045 = 731 at 28%) is still inside the share ceiling used for capex. Caveat: k was measured on one product in one segment (LT); it may not carry to HT. Edge first sells in the R2 year (Jul 1 launch), so k on Edge is measured in practice rounds PR2-PR3 (D), well before CR1 on Oct 28: if PR2-PR3 show Edge's actual HT share below 25% in a field where at most one rival has a young HT product, the CR1 plan switches to B.
- **Bear case (rival-driven: Edge 25% while B keeps 31%).** R3: 933 Edge units (630 first + 303 second): revenue $40.1M, cost 630 x 29.92 + 303 x 34.40 = $29.3M, CM $10.85M. Eat CM $7.2M. Total $18.05M, less fixed 10.56 = pre-tax about $7.5M, about equal to B's $7.8M, with $11M more capital employed. So A pays only if Edge holds about 28-30% of HT or more. (Earlier versions printed $28.8M/$11.3M here: an arithmetic slip, now corrected.) Mitigation: (a) the R1 line purchase is gated on the revision date; (b) the R2 purchase is gated on FastTrack showing fewer than 2 rival young HT products in the HT fine cut; (c) the fallback is B.
- **Gates extended (round 2).** Because the bear case equals B on profit with $11M more capital, every Edge capacity purchase from R4 is capped by Edge's MEASURED potential HT share (ceiling table in section C), not by the 36% plan; the R7 purchase is cancelled; Eat's repositions are the cheapest fine-cut fix (A16).
- B is the fallback. If the R&D screen shows Edge's revision later than Jul 1 R2 and no fix works, or the capex breaks the worst case, move Eat to HT (B) and put capex into Eat's line.

### Barriers rivals cannot cheaply copy
- Capacity bought a year ahead (a rival that sees Edge in FastTrack in R2 can buy no sooner than R3; its line lands in R4).
- Edge's annual repositioning keeps age about 1.0-1.5 where rivals' repositioned products start at 2+.
- Accumulated awareness/accessibility in HT (decays 1/3 per year, so latecomers pay a lot).
- Framework barriers: capacity/automation investment and economies of scale.

### Scoring under rank-based vs Balanced Scorecard grading
- **Rank-based:** A wins by profit scale R4-R8 if Edge holds its share. R1-R3 dilution (300K new shares, 15%), the zero R1 dividend and leverage may hurt the early stock price; the price formula coefficients are NOT IN DATA, so any claim that it recovers is unsupported. PR1-PR2 test this: read the Finance screen's EPS and stock price with dividend $0 vs $1,000K (D). Maximize cumulative profit and ending stock price; dividends up to EPS from R5 (dividends above EPS are ignored by the price formula).
- **BSC:**
  - Financial: leverage about 1.6-2.0 (rises in R1, est. 1.8, then falls).
  - Internal: blended CM vs the instructor's 30%: R2 27%, R3 27%, R4 25%, R5 23%, R6 21%, R7 17%, R8 15% (average about 22%, gap about 8 points). How the BSC converts that gap into points is NOT IN DATA, so it cannot be priced. Cheap levers if BSC weighs CM heavily: Edge at $45 (+$1 x units, about +$2.8M in R7), skip the R7 reposition (about +$2.1M pre-tax; its lost CSS is roughly $1.6M by a rough estimate, so near break-even), no R7 capex (done). Plant utilization high; days of working capital low conflicts with 60-day A/R.
  - Customer: awareness, accessibility, buying-criteria fit, product line breadth (two products across two segments).
  - Learning and growth: HR effects NOT IN DATA.
- **Where they conflict:** BSC rewards awareness/accessibility and breadth (cost money, lower profit); BSC rewards low working-capital days and low idle cash, rank rewards profit and stock price; idle cash is the emergency-loan buffer. Resolution: modest awareness/accessibility spend, no 90-day terms, and pay cash out as dividends from R5, sized to the worst-case test (idle base cash equals the shock buffer, A18).

## C. Round-by-round plan (CR1-CR8)

All numbers are plan-case targets under A1-A15. Recalculate each round from live screens.

### Products and positions (target = previous year-end ideal; sells at old specs until the revision date)

| Round | Eat (LT) R&D | Edge (HT) R&D |
|---|---|---|
| R1 | 5.3/14.7, MTBF 20,000. Single-project rev about Nov 9, $860K (A14: budget $1.0M); material about $12.00; age 2.1 at year-end | NEW, 8.1/11.9, MTBF 23,000, automation 3. Start Jan 1; single-project about 15.6 months (A5), $1.0M in R1 |
| R2 | No project (age 2.1 -> 3.1) | Launch on the R&D-screen date (base case Jul 1, A17). Age at year-end about 0.7 |
| R3 | None (Eat at 5.3/14.7 is 1.41 from the R3 LT center, inside the fine cut) | Reposition to 8.8/11.2 (0.99, about 6.0 months by the A5 fit, rev about Jul 1, $520K) |
| R4 | Reposition to 5.9/14.1 (d 0.85, about 5 months, rev about Jun 8, about $0.43M; book point: material $14.54, A16). Keeps Eat inside the fine cut through R5 (R5 year-end distance 1.98). | Reposition to 9.5/10.5 (about Jul 1, $520K) |
| R5 | None | Reposition to 10.2/9.8 (optionally start Edge II, launch R6) |
| R6 | Reposition to 6.9/13.1 (d 1.41 from 5.9/14.1, about 8.9 months, rev about Sep 25, about $0.75M; book point: material $16.44). In cut R6-R8 (R7 year-end distance 1.98; R8 2.69 only at year-end). | Reposition to 10.9/9.1 |
| R7 | None | Reposition to 11.6/8.4 only if the displayed revision date is before Aug 1 |
| R8 | No R&D | No R&D (a late revision gives no payoff in the game) |

- Edge's age with a Jul 1 revision each year: age at revision about 1.0, year-end about 1.5 (fixed point of a = (a + 0.5)/2 + 0.5). HT age score at 1.0-1.5 is about 60-74.
- Priority rule when projects overlap (R4, R6): Edge first. Eat's project is cancelled or moved to a smaller step if it lengthens Edge's date past Jul 31; Eat's fine-cut exit is the only reason to run it.
- LT rule (round 3 wording): start an Eat reposition in the round in which its distance to the LT center at the (displayed) revision date would exceed 2.5, or its year-end distance would exceed 2.7. Outside the fine cut by a small amount costs about 1% of Eat's score (brief: -1% just outside), so a few weeks at 2.5-2.7 is accepted; moving Eat a round earlier would bring forward the material rise of A16 (R6 to 6.9/13.1 one year early: +$1.90/unit x 800 = about $1.5M) to avoid about 2 months at about -1% to -5%. Check on the R6 case: Eat at 5.9/14.1 is 2.49 from the center on Sep 25 R6 (just inside), 2.69 at R6 year-end; after the revision to 6.9/13.1 the distance is 1.27 at R6 year-end, 1.98 at R7 year-end and 2.69 only at R8 year-end. Eat's age: 2.1 at R1 end, 3.1 R2, 4.1 R3; the R4 reposition halves it (age is not a problem: LT age ideal 3.0).
- Edge position target (round 3): each Edge reposition aims at the PREVIOUS year-end ideal (step 0.7, constant). With a Jul 1 revision this lags the drifting ideal: 0.7-1.05 behind in H1 on the old spec, 0.35-0.7 behind in H2. Aiming at the SAME-year year-end ideal instead would cut the lag to at most 0.35 (the mean-matching point over a Jul 1 to Jul 1 hold), but shifts the whole path one step toward the leading edge: material +$1.12/unit on all Edge units (A15), about $2.2M in R5 on 1,935 units. Break-even: that needs CM +10.7% = units +9% = CSS about +14% = raw +9.7 of 69 = about +29 position points (position weight 33%). Position score within the fine cut is NOT IN DATA, so the plan keeps the cheaper path and PR3 tests the alternative (D); adopt it only if the measured Dec CSS gain exceeds +14% of Edge's CSS.

### Prices, marketing, capacity, financing (targets)

Eat price is a hedge, not an optimum: R1 $32 (price score about 11), R2-R8 $30 (score 20); the price curve is measured in PR1-PR3 (section D) and replaced by what the CM-dollar maximum shows. Edge prices are the single biggest sensitivity: start at the values below, test, and move in $2 steps.

| R | Eat price | Edge price | Promo (Eat / Edge) $K | Sales (Eat / Edge) $K | Edge first-shift capacity at year start | Capacity bought this round | Financing |
|---|---|---|---|---|---|---|---|
| 1 | $32 | n/a | 1,500 / 0 | 1,000 / 0 | 0 | Edge +330 @ auto 3 = $5,940K | Bonds $2,480K, stock 100K shares $1,117K, current debt $7,000K, dividend 0 (see D for the $1,000K alternative) |
| 2 | $30 | $42 | 1,000 / 1,500 | 1,000 / 1,500 | 330 | Edge +300 = $5,400K (gated) | Bonds $4,000K (cap $4,851K), stock 100K shares, current debt $7,500K (limit about $8.8M), repay $867K bond (2028) |
| 3 | $30 | $43 | 1,000 / 1,500 | 1,000 / 1,500 | 630 | Edge +300 = $5,400K | Bonds $4,000K (cap about $4,086K), stock 100K shares, current debt rolled at $7,500K (limit about $8.4M; NOT $9,500K) |
| 4 | $30 | $44 | 1,000 / 1,500 | 1,000 / 2,000 | 930 | Edge +400 = $7,200K (capped by measured share, below) | No bonds; current debt up to $11,000K (limit about $15.9M); repay $1,733K bond (2030); dividend 0 |
| 5 | $30 | $44 | 1,000 / 1,500 | 1,000 / 2,000 | 1,330 | Edge +300 = $5,400K (capped by measured share) | Roll current debt $11,000K; dividend $2.5M |
| 6 | $30 | $44 | 1,000 / 1,500 | 1,000 / 2,000 | 1,630 | None | Repay $2,600K bond (2032); roll current debt $11,000K; dividend $5.0M |
| 7 | $30 | $44-45 | 1,000 / 1,500 | 1,000 / 2,000 | 1,630 | None (payback rule below) | Repay $2,000K current debt (to $9,000K); dividend $4.5M |
| 8 | $30 | $44-45 | 1,000 / 1,500 | 1,000 / 2,000 | 1,630 | None | Repay $4,000K current debt (to $5,000K); dividend $4.5M; more dividend/retirement only by the release rule in A18 (stock-retirement cost = shares x price x 1.015; price NOT IN DATA) |

- R7 capacity rule (changed in round 2): the +150 purchase is CANCELLED. Test: R7 spend of +150 x $18 = $2,700K buys one year of benefit (R8 only): 150 units of second shift ($39.44) become first shift ($34.96) = $4.48 x 150 = $0.67M, plus about 84 extra units that exceed 3,260 capacity at about $5 CM = $0.43M. About $1.1M benefit vs $2.7M outlay (depreciation $180K + financing about $270K in R8 alone; whether the 65% resale counts toward the score is NOT IN DATA). Fails; R8 Edge output is capped at 3,260 (1,630 first + 1,630 second). R6 also buys nothing: capacity 1,630 covers R7's 2,786 units (second shift 71%).
- Edge capacity ceiling by measured share (applies to the R4 and R5 purchases; capacity available next year <= 0.70 x measured potential HT share x next-year HT demand; 0.70 matches the plan's first-shift/second-shift mix):

| Purchase round | Capacity for | HT demand | At 36% (plan) | At 30% | At 25% | Plan buy |
|---|---|---|---|---|---|---|
| R4 (cap for R5) | R5 | 5,375 | 1,355 | 1,129 | 941 | +400 (to 1,330) |
| R5 (cap for R6) | R6 | 6,450 | 1,625 | 1,355 | 1,129 | +300 (to 1,630) |

  At 30% buy R4 +200 (to 1,130) and R5 +225 (to 1,355); at 25% buy R4 +10, R5 +190. "Measured share" = Edge's actual-vs-potential share in the latest FastTrack (potential if stocked out). A second check: second-shift use of Edge in the last round must exceed 40%.
- Price logic is A1-based and unverified: with share = c/(c+R), a $1 move changes raw CSS only 1-2 points near the top of the range, so unit margin dominates **if** rival CSS is flat. This fails if rivals cut price or have better CSS. Edge at $42-44 has a price score of only about 9 at $43 (interpolating the brief's $40 -> 20 and $45 -> 1); that is already inside the raw 69 used above, so the Edge price is a bet on position and age carrying the score. Worked Edge example (A1): $34 -> $40 moves raw 78.9 -> 72.4, CSS 52.9 -> 48.5, share 39.8% -> 37.7%, units 1,238 -> 1,174 on 3,110; contribution at cost $29.4: (34-29.4) x 1,238 = $5.7M vs (40-29.4) x 1,174 = $12.4M. For LT the same model gives a smaller win and the price weight is 41%, not 25%; that is why Eat sits at $30-32 and not at $35 (score about 1).
- Do not price LT outside the range ($35) unless a seller's market is verified (up to $9.99 above range sells when industry capacity cannot meet demand).
- Awareness: $1.5M promo adds about 36 points vs about 18 at $1M (inferred from the 55% steady state and "start = last year x 2/3"); CSS +11.6% for $0.5M. Above $3M wasted.
- Accessibility: LT at $1M holds about 40%; $2M adds about 9 points (+6.4% CSS for $1M), not worth it for one Eat product. Edge starts at 41% x 2/3 = 27% and needs $1.5-2.0M. Edge II (2+ products) later enables 100% accessibility (about $3.5M combined maintains it).

### Cash math (plan case; screen numbers decide; $K; A/R 30 days so 11/12 of a year's revenue change collects in-year)

**R1.** Base is the screen's $4,470K projected cash at default (1,122 units at $34, production 1,287).

| Step | $K | Running |
|---|---|---|
| Screen projection | 4,470 | 4,470 |
| Sales: 1,220 x $32 = 39,040 vs 1,122 x $34 = 38,148: +892 x 11/12 | +818 | 5,288 |
| Production type-in 1,290 (produces 1,277) vs 1,287 (1,274): 3 x 26.57 | -80 | 5,208 |
| Dividend cut (A3) | +1,000 | 6,208 |
| R&D: Eat 1,000 (A14) + Edge 1,000 | -2,000 | 4,208 |
| Promo +500 | -500 | 3,708 |
| Bonds 2,480 net of 5% = 2,356, less full-year interest 248 | +2,108 | 5,816 |
| Stock 100K x $11.17 = 1,117, net 5% | +1,061 | 6,877 |
| Current debt 7,000 less interest at 8.6% = 602 | +6,398 | 13,275 |
| Capex Edge +330 x $18 | -5,940 | **7,335** |

- Worst case (sales 1,000, -220 units; production still from best case): -220 x 32 x 11/12 = -6,453 gives **$882K**. Positive: no emergency loan.
- Why the mix: current debt (8.6%, no fee) is cheapest, stock the smallest piece that still passes the worst case. Without any stock, debt would need to be about $8.07M, 92% of the A10 limit, too tight. **Plan Y** (if the screen's current-debt limit is under $8.0M): stock 200K ($2,122K net) + current debt $6,000K gives base $7,482K, worst $1,029K.
- Bond check: 5,200 + 2,480 = 7,680 = 80% x 9,600. Pass. Leverage about 1.8-2.0. Max investment must be >= 5,940.
- Gates: (1) Edge revision later than Jul 1 R2 after the section D decision tree: do not buy the line, switch to B. (2) Idle-line cost if launch slips: depreciation $396K + financing about $550K = about $0.95M/yr plus lost Edge CM of about $0.57M per month of delay (R2 half-year CM $3.4M).

**Model used for R2-R8 (round 3, one consistent model).** Per round: CM (section C case values) less fixed costs excluding interest (R2 7.71, R3 8.43, R4 9.38, R5 9.63, R6 10.72, R7 9.97, R8 9.45 $M: marketing, R&D, depreciation, admin, other), less interest = 10% x bonds outstanding after maturities and new issue + 8.6% x current debt balance (A19), tax 35% (A4), plus depreciation, less working-capital build (R2 0.16, R3 3.0, R4 1.5, R5 1.1, R6 1.4, R7 1.7, R8 1.0). Worst case = closing cash less 18% x revenue x 11/12 (A18). Bond cap = 80% x net fixed assets at the start of the year less bonds outstanding. A 15-line script reproduces every table below to the nearest $K; the team should rebuild the same logic in a spreadsheet and replace each input with the live screen value.

**R2.** Edge launch assumed Jul 1 (half-year: 165 first-shift + 165 second-shift = 330 units; single-project Apr 19 would give 462, an upside). Revenue $40.9M.

| Item | $K |
|---|---|
| Opening cash (base) | 7,335 |
| Bond maturity (2028) | -867 |
| CFO (below) | +2,277 |
| New bonds $4,000K, net of 5% | +3,800 |
| Stock 100K shares at $11.17, net of 5% | +1,061 |
| Current debt rolled $7,000K to $7,500K | +500 |
| Edge capex +300 x $18 | -5,400 |
| **Closing (base)** | **8,707** |

- CFO: Eat 900 units at $30: revenue $27.0M, cost 800 x 20.96 + 100 x 25.44 = $19.3M, CM $7.7M. Edge 330 units at $42 = $13.9M; cost 165 x 29.4 + 165 x 33.9 = $10.4M; CM $3.4M. Total CM $11.1M (27.2%). Fixed excluding interest $7.71M; interest $1.73M (bonds 10,813 x 10% = 1.08, current debt 7,500 x 8.6% = 0.65). Pre-tax $1.66M, net $1.08M, plus depreciation $1.36M, less working capital $0.16M = $2.28M.
- Worst case (-18% revenue: -$7.36M x 11/12 = -$6.75M): **$1,958K**. Pass. (Round-2 version printed $620K because it omitted $400K of interest on the new bonds and used no extra debt.)
- Gate for the R2 capex: if Edge's revision is after Jul 1 (CM lost about $0.57M/month), cut the +300 until the worst case is >= $500K (zero capex if the revision is Oct 1 or later).
- Bond headroom at R2: 80% x net fixed assets $14,580K = $11,664K less outstanding $6,813K = $4,851K. Issue $4,000K. Current debt $7,500K is 85% of the about $8.8M limit (A10).

**R3.** Revenue $76.9M.

| Item | $K |
|---|---|
| Opening | 8,707 |
| CFO | +5,244 |
| Bonds $4,000K net of 5% | +3,800 |
| Stock 100K shares, net | +1,061 |
| Current debt rolled at $7,500K (no increase: limit about $8.4M) | 0 |
| Edge capex +300 x $18 | -5,400 |
| **Closing (base)** | **13,412** |

- CFO: Edge 1,230 units (630 first + 600 second) at $43 = $52.9M; cost: material 20.4 + 0.56 (A15) = 20.96, first-shift 29.92, second 34.40: 630 x 29.92 + 600 x 34.40 = $39.5M; CM $13.4M. Eat 800 at $30: 800 x (30 - 20.96) = $7.2M. Total CM $20.6M (26.8%). Fixed excluding interest $8.43M; interest $2.13M (bonds 14,813 x 10% = 1.48, current debt 7,500 x 8.6% = 0.65). Pre-tax $10.04M, net $6.53M, plus depreciation $1.72M, less working capital $3.0M (revenue +$36M, A/R +$3.0M) = **$5.24M**.
- Worst case (-$13.84M x 11/12 = -$12.69M): **$724K**. Pass; this is the tightest round. If the live worst case is under $500K: cut capex first, then ask for a third stock tranche (max 20% of shares = 400K) before touching dividends (there are none).
- The earlier version borrowed $9,500K of current debt here (+$2.5M), 13% above the brief's limit formula given this plan's own R2 sales; corrected above (A10).

**R4.** (Eat reposition $0.43M and lower Eat CM; the 2030 bond maturity is now in the table.) Revenue $94.8M.

| Item | $K |
|---|---|
| Opening | 13,412 |
| CFO | +8,549 |
| Bond maturity (2030) | -1,733 |
| Current debt $7,500K to $11,000K | +3,500 |
| Edge capex +400 x $18 (capped by measured share) | -7,200 |
| Dividend | 0 |
| **Closing (base)** | **16,528** |

- CFO: Edge 1,610 units (930 first + 680 second) at $44 = $70.8M; material 20.4 + 1.68 = 22.08, first 31.04, second 35.52: cost 930 x 31.04 + 680 x 35.52 = $53.0M; CM $17.8M. Eat: material 0.44 x 12.00 + 0.56 x 14.54 = 13.42 (A16), first-shift cost 22.38, CM (30 - 22.38) x 800 = $6.1M. Total $23.9M on $94.8M (25.2%). Fixed excluding interest $9.38M (marketing 5.5; R&D 0.52 + 0.43; depreciation 2.08; admin 0.85); interest $2.25M (bonds 13,080 x 10% = 1.31, current debt 11,000 x 8.6% = 0.95). Pre-tax $12.27M, net $7.97M, plus depreciation $2.08M, less working capital $1.5M = $8.55M.
- Worst case (-$17.07M x 11/12 = -$15.64M): **$886K**. Pass. No bonds in R4 (5% fee plus 10% coupon on money that would sit as a buffer); the buffer is current debt at 8.6% with no fee, well inside the about $15.9M limit (69%). The earlier R4 dividend of $1.0M funded by fee-bearing bonds is dropped.

**R5.** Revenue $109.1M.

| Item | $K |
|---|---|
| Opening | 16,528 |
| CFO | +10,241 |
| Edge capex +300 x $18 (capped by measured share) | -5,400 |
| Current debt rolled at $11,000K | 0 |
| Dividend ($1.09/share on 2,300K shares; EPS about $3.8) | -2,500 |
| **Closing (base)** | **18,869** |

- CFO: Edge 1,935 units (1,330 first + 605 second) at $44 = $85.1M; material 23.2, first 32.16, second 36.64: cost $64.9M; CM $20.2M. Eat: material 14.54, first-shift cost 23.50, CM 6.50 x 800 = $5.2M. Total $25.4M on $109.1M (23.3%). Fixed excluding interest $9.63M; interest $2.25M. Pre-tax $13.52M, net $8.79M, plus depreciation $2.56M, less working capital $1.1M = $10.24M.
- Worst case (-$19.6M x 11/12 = -$18.0M): **$868K**. Pass. If Edge's measured share is under 33% the capex shrinks (ceiling table) and the dividend can rise by the saved amount.

**R6.** Revenue $126.2M.

| Item | $K |
|---|---|
| Opening | 18,869 |
| CFO | +10,542 |
| Bond maturity (2032) | -2,600 |
| Current debt rolled at $11,000K | 0 |
| Dividend ($2.17/share; EPS about $3.9) | -5,000 |
| **Closing (base)** | **21,811** |

- CFO: Edge 2,322 units (1,630 first + 692 second) at $44 = $102.2M; material 24.32, first 33.28, second 37.76: cost $80.4M; CM $21.8M. Eat: material 0.73 x 14.54 + 0.27 x 16.44 = 15.05, first-shift cost 24.01, CM 5.99 x 800 = $4.8M. Total $26.6M on $126.2M (21.1%). Fixed excluding interest $10.72M (R&D 0.52 + 0.75); interest $1.99M (bonds 10,480, current debt 11,000). Pre-tax $13.89M, net $9.03M, plus depreciation $2.92M, less working capital $1.4M = $10.54M.
- Worst case (-$22.7M x 11/12 = -$20.8M): **$988K**. Pass.

**R7.** Revenue $146.6M.

| Item | $K |
|---|---|
| Opening | 21,811 |
| CFO | +9,996 |
| Repay current debt (to $9,000K) | -2,000 |
| Dividend ($1.96/share) | -4,500 |
| **Closing (base)** | **25,308** |

- CFO: Edge 2,786 units (1,630 first + 1,156 second) at $44 = $122.6M; material 25.44, first 34.40, second 38.88: cost $101.0M; CM $21.6M. Eat: material 16.44, first-shift cost 25.40, CM 4.60 x 800 = $3.7M. Total $25.3M on $146.6M (17.3%). Fixed excluding interest $9.97M (R&D 0.52, no Eat project, no new capex); interest $1.82M. Pre-tax $13.51M, net $8.78M, plus depreciation $2.92M, less working capital $1.7M = $10.0M.
- Worst case (-$26.4M x 11/12 = -$24.2M): **$1,119K**. Pass. The dividend is sized to this test.
- Margin response if Edge first-shift CM < 20%: skip the R7 reposition (saves $0.52M R&D and stops the material rise) and price Edge at $45.

**R8 (harvest).** Edge 3,260 units (1,630 first + 1,630 second, 100% second-shift use) at $44 = $143.4M; material about 26.0 (no R8 reposition), first-shift 34.96, second 39.44: cost $121.3M; CM about $22.1M. Eat 800 at $30 with cost 25.40: $3.7M. Total CM about $25.8M on $167.4M (15.4%). Fixed excluding interest $9.45M; interest $1.48M (bonds 10,480; current debt 5,000). Pre-tax $14.87M, net $9.67M; CFO $11.58M. Opening $25.3M, repay current debt $4.0M, dividend $4.5M ($1.96/share vs EPS $4.2): closing $28.4M, worst case (-18%: -$30.1M x 11/12 = -$27.6M) **$769K**. Pass. The $28.4M is the 18% shock buffer; if measured forecast errors are small the release rule (A18) lets the last payout rise, e.g. s = 10% frees about $12M for dividends or stock retirement. Payout above EPS is ignored by the price formula, so only the part up to EPS helps the stock price.

### Targets by round

| R | CM target (plan) | Share target | Ending cash (base / worst) |
|---|---|---|---|
| 1 | >= 17% at the screen (blend; 21.8% appears only at $34) | about 15% | $7.3M / $0.9M |
| 2 | >= 26% | about 12% of industry | $8.7M / $2.0M |
| 3 | >= 26% | about 14% | $13.4M / $0.7M |
| 4 | >= 25% | about 15% | $16.5M / $0.9M |
| 5 | >= 23% | HT 33%+ | $18.9M / $0.9M |
| 6 | >= 21% | HT 33%+ | $21.8M / $1.0M |
| 7 | >= 17% | HT 33%+ | $25.3M / $1.1M |
| 8 | >= 15% | harvest | $28.4M / $0.8M (after repayment and dividend) |

The instructor's 30% CM is not reachable after R2 with this plan (second-shift labor, Edge and Eat material creep). The per-unit floors below, not the blended percentage, are the price-war rule. First-shift Edge at $42 reaches 30% at launch only.

## D. Practice Round 1: exact decisions, screen by screen

Today is Oct 10; PR1 closes 10/11 11:30 PM, tz unconfirmed. Treat the earliest plausible timezone as the deadline and finish the first save about 12 hours earlier.

**R&D**
- Enter both projects at once: Eat 5.3/14.7, MTBF 20,000; and new product "Edge" at 8.1/11.9, MTBF 23,000, automation 3. NOT IN DATA: where new-product and line-purchase inputs live; read the screen.
- Read both revision dates and costs (multi-project lengthening, A14). Decision tree:
  1. Edge <= Jul 1 R2 and Eat <= Dec 1: proceed.
  2. Edge > Jul 1 R2 with both: delete Eat's project, re-read Edge's date. If Edge alone is <= Jul 1, run Eat at a smaller move (5.9/14.1: book May 3, $340K, material $14.54, saves $1.43/unit) and re-check; if that still delays Edge, drop Eat's project and plan its R1-style move for R2 or R3 (cost: $3.4M/yr saving deferred, still positive).
  3. Edge alone is also > Jul 1 R2 (Oct 1 or later): do not buy the line; switch to B (move Eat to HT) and re-price the cash.
- Record Edge's material cost. If it is > $21.5, re-run the margin table before buying.

**Marketing (Eat)**
- Price $32 (inside the LT range; score about 11; screen CM 17.0%, accepted: the realised R1 CM is a blend with the cheaper material from Nov 9). This is a hedge between the A1 optimum and the LT price-war risk (section C); it is replaced by measurements in PR2-PR3.
- Promo $1,500K. Sales budget $1,000K. A/R 30 days. "Your Forecast" = 1,250.

**Production** (one decided number)
- Eat: forecast F = 1,250. Available target = 1,250 x 12/11 = 1,364. Less inventory 87 = 1,277. Divide by 0.99 (1% A/P withholding at 30 days) = **1,290** typed. Second shift about 61% of first-shift capacity (800 + 490).
- Inventory outcomes at 1,364 available (1/6 limit = 227): forecast 1,250 leaves 114 (pass); best case 1,356 leaves 8 (pass, no stock-out); worst case 1,000 leaves 364, above the 227 limit (breach by design: the brief tells me to set production from the best case and test cash at the worst case). Carrying cost at worst: 364 x 26.57 x 12% = $1.16M, accepted; a stock-out sends customers to rivals.
- A/P 30 days. Buy Edge capacity +330, automation 3 ($18/unit = $5,940K). Keep Eat automation 3.0.

**HR.** Defaults: complement 250, wage $20/hr, benefits $2,500, profit sharing 2%, recruiting $0, training 0 hours. HR effects NOT IN DATA. Check that the screen does not flag a labor shortfall at 1,277 units; if it does, hire to the stated need.

**Finance.** Bonds $2,480K. Stock 100K shares ($1,117K). Current debt $7,000K (check the screen's limit; if under $8.0M use Plan Y: stock 200K, current debt $6,000K). Dividend $0 (cash-driven: with the default $1,000K dividend the R1 worst case is -$118K, a fail). Alternative if the stock-price test below shows a larger price penalty from dropping the dividend than the cost of extra shares: dividend $1,000K plus stock 200K shares (base $7,396K, worst $943K). Retire nothing.

**Pre-save checks (all must pass)**
1. Revision dates and R&D cost for Eat and Edge match the decision tree above.
2. Eat CM >= 17.0% on the Production screen at $32 (cost $26.57, (32 - 26.57)/32). The screen does not show the $12.00 material until the Nov 9 revision; 21.8% appears only at $34.
3. Dec 31 cash with "Your Forecast" = 1,000 is >= $500K while the production type-in stays 1,290.
4. Inventory: at forecast 1,250 and at best case 1,356, end units are >= 1 and <= 1/6 of available (227). The worst-case breach is accepted only because check 3 passes.
5. Bonds + existing <= the cap on screen. Max investment >= capex.
6. Edge line bought at automation 3 (nothing else touched).
7. A second member reads every screen aloud. One saver clicks File > Update Official Decisions and records the time.

### What each practice round should test (the sim resets after PR5)

- **PR1 (full R1 plan, Eat $32).** Calibrate actual Dec CSS vs A1; the Edge date/cost/material with both projects entered; max-investment behavior (A9); the dividend default (A3) and the stock price/EPS the Finance screen shows with dividend $0 vs $1,000K (A20); the live current-debt limit (A10: compare it with the formula, then size R2-R3 debt at 89% or less of it); actual rival moves.
- **PR2.** Edge sells for the first time (launch year): measure Edge's actual HT share and k = actual/modelled CSS on Edge itself (section B); this decides A vs B before CR1. Price elasticity with one clean step each: Eat $35 (vs PR1's $32), Edge $42 vs $38. Test promo $1.5M vs $1.0M. Confirm the Edge launch date and output before/after the revision date.
- **PR3.** Eat $29 (third point on the LT price curve; choose the price that maximizes CM dollars, not share). A/R 60 days: CSS change (rule: +6.3 points over 30 days) vs cash hit. Edge annual reposition: date, cost, age after; with and without a simultaneous Eat project. Edge position test: run the same year once with the target at the previous year-end ideal (plan) and once at the same-year year-end ideal; adopt the second only if Edge's Dec CSS rises by more than 14% (break-even, section C).
- **PR4.** Capacity scale-up for R4: second-shift limits, stock-out behavior, inventory range. Dividends and current-debt rollover.
- **PR5.** Full dress rehearsal of workflow, roles, timing and save protocol. Read rival habits in FastTrack for CR1 (A11).

## E. Adapting each round from the new FastTrack

Read in this order: (1) perceptual map (rival positions vs segment ideals); (2) CSS by segment (Dec survey); (3) actual vs potential share; (4) rival capacity and automation; (5) stock-outs; (6) published growth rates; (7) rival prices, promo and sales budgets.

| If the data shows... | Do this |
|---|---|
| Two or more rivals have a young product in the HT fine cut | Treat the Edge share assumption as failed: skip the next capex step, keep Edge's annual reposition, add promo/sales on Edge, consider Edge II, hold price (cut in $2 steps only if actual share < potential share) |
| One rival launches or repositions toward HT | Keep the annual reposition, add promo/sales on Edge, hold price |
| Rivals cut LT prices | Hold the Eat price. Accept lower share. Eat first-shift unit CM < 15% of price is not worth the volume. Eat's second shift only pays while material is near $12-14 (second-shift cost = material + $13.44: at $12.00 CM $4.56, at $14.54 $2.0, at $16.44 $0.1); LT potential share (about 1/6 of LT demand, 1,100 units in R3, 1,800 in R8) exceeds Eat's 800 first-shift units, so use Eat second shift in R2-R4 when stock-outs or potential share show demand left |
| A rival adds large capacity (seller's market ending) | Cancel or shrink next year's capex; keep cash |
| A seller's market is confirmed (industry capacity < segment demand) | Raise price up to $9.99 above range; build inventory only up to the 1/6 rule |
| We stocked out (actual share < potential share) | Raise next year's production and capacity; forecast from potential share x next year's demand |
| Inventory > 60 days | Lower the schedule, raise price $1-2, avoid cutting promo |
| Growth rates change | Recompute the demand table; resize capex before the Dec 31 cash check |
| Worst-case cash < $500K | In order: cut capex; add current debt; cut dividend; cut promo; delay bond/stock timing |
| Edge's CSS < rival HT CSS despite a good position | Check age (reposition earlier), price, MTBF (23,000), awareness |
| Edge first-shift CM < 20% | Skip the next reposition, raise price toward $45, check automation 4 only if R&D time is unchanged |

Forecast method: December CSS share x next year's demand, adjusted for competitor moves; always override the benchmark (it assumes every rival has one CSS-20 product per segment).

## F. Top risks (pre-mortem) and prevention

1. **Emergency loan** (current debt rate + 7.5%, depresses stock price). Prevention: worst-case check at -18% volume with production from the best case; current debt as pre-arranged insurance; worst-case margins are thin in R1-R5 ($0.7-2.0M), so any R&D date slip must trigger a capex cut first. Current debt is held below 90% of the formula limit (A10) so the plan cannot borrow what the sim will refuse.
2. **Edge launch delayed** (A5, A14; revision after Jul 1 R2). Cost about $0.95M/yr idle line plus about $0.57M CM per month. Prevention: section D decision tree; gate the R1 and R2 capex.
3. **Edge share below 30%** (rival young HT entrants). A then equals B at R3 on profit with $11M more capital. Prevention: R2 FastTrack gate, share-ceiling table on the R4 and R5 purchases, R7 purchase cancelled, section E.
4. **Stock-out.** Prevention: schedule = (F x 12/11 - inventory) / (1 - withholding); second shift as buffer.
5. **Overstock** (12% carrying cost; days > 60). Prevention: forecast from potential share; inventory <= 1/6 check at the forecast case.
6. **R&D overrun / multi-project slip.** Prevention: use displayed dates; reposition in small steps; Edge has priority over Eat.
7. **Price war.** Prevention: different game in each segment; do not chase; per-unit floors: Eat first-shift CM >= 15% of price, Edge first-shift CM >= 20% of price (blended CM is an output, 15-27% in this plan).
8. **Margin creep on Edge** (material +$1.12 per reposition, price capped at $45). Prevention: A15 tracking, skip late repositions.
9. **Overcapacity / idle fixed cost.** Prevention: capacity only against a verified demand gap; R7 rule sizes the last purchase.
10. **Over-leverage.** Prevention: bonds <= 80% of net fixed assets; track leverage; repay current debt from R7 (the 2030 and 2032 maturities are in the cash tables).
11. **Save collision.** Prevention: protocol in G.
12. **Model risk (A1).** Prevention: PR1-PR3 calibration; every price number is a starting point.
13. **Deadline/timezone.** Prevention: finish early.

## G. One-page summary

**Strategy.** Eat to LT as a cheap cash cow in R1 (material $15.97 -> about $12.00, MTBF 20,000, price $30-32 not $35). New HT product Edge from R1 (8.1/11.9, MTBF 23,000, automation 3). Edge launches by about Jul 1 R2 and is repositioned every year by about 0.7 (target = previous year-end ideal), except R8. Buy Edge capacity a year ahead: +330, +300, +300, +400 and +300 (the last two capped by measured share), 0, 0. Edge price $42-44. Eat repositions only to keep the fine cut (R4 to 5.9/14.1, R6 to 6.9/13.1). Cash buffers via the worst-case check every round (-18% is an ASSUMPTION, A18). Current debt never above the brief's limit formula (A10): $7.0M R1, $7.5M R2-R3, $11.0M R4-R6.

**Sequence.** R1: reposition + invest + finance (bonds max, stock 100K, current debt $7.0M, no dividend). R2: launch + capacity + bond maturity + bonds $4.0M + stock 100K. R3: capacity + bonds $4.0M + stock 100K. R4: capacity + current debt to $11.0M + 2030 bond maturity. R5-R7: dividends ($2.5M, $5.0M, $4.5M) sized to the worst-case test; 2032 maturity in R6; current debt repaid from R7. R8: repay $4.0M, dividend $4.5M, harvest.

**Numbers to remember.** Capacity cost = $6 + $4 x automation per unit. Bond cap = 80% of net fixed assets. Stock cap = 20% of shares. Reposition time about 6.7 x distance - 0.6 months for d >= 0.7 (book-point fit, A5; read the screen). Schedule typed = (F x 12/11 - inventory) / (1 - withholding). Edge material rises about $1.12 per yearly reposition.

**Owners (5 members).**
- R&D and Production lead: R&D targets, schedule, capacity.
- Marketing lead: price, promo, sales, A/R terms.
- Finance lead: financing, Dec 31 worst-case cash, bond/stock caps.
- HR and analytics lead: HR screen; FastTrack reading; model calibration (A1).
- Captain and saver: deadlines, the single save, change log.

**Save protocol.**
1. After FastTrack: 60-minute analysis meeting; fill the decision sheet.
2. Edit in a fixed order: R&D, Marketing, Production, HR, Finance (Finance last; projections depend on the rest).
3. Everyone else stops editing; one person touches the sim.
4. Second-person read-aloud against the pre-save checks (section D).
5. One saver clicks File > Update Official Decisions, records the time, screenshots each screen.
6. Save at least 12 hours before close; a later re-save only by the captain.

## H. NOT IN DATA / verify in the spreadsheet or screens

- The scoring method for the 15% team score (rank vs BSC).
- The CSS formula and the position-score curve (A1); rough-cut radius; age curve beyond the quoted points; segment drift beyond R8.
- New-product R&D time and cost (A5 is a proxy); the -18% shock (A18); the multi-project lengthening size (A14); line-purchase inputs; whether capacity can be added to a line in increments (A14).
- HR/TQM effects; annual raise; the dividend default (A3); tax rate (A4); interest on cash.
- Rival behavior (A11).
- Material costs beyond the book points (A6, A15, A16).
- Stock price formula coefficients.
- Whether max investment, bond cap and current-debt limit move with other decisions (A9, A10).
- Whether the 65% capacity resale counts toward the final score.
- Existing-bond coupons (A19); the issue price of later stock (A20); the position-score curve inside the fine cut (needed to price the Edge target choice); whether the current-debt limit uses year-end A/R and last year's cost as read in A10.
