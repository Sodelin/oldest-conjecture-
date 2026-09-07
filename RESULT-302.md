# Verified plateau at 732 for Erdős problem 302

Let f(n) be the largest size of a subset S of {1,...,n} containing no three distinct
integers a,b,c with 1/a = 1/b + 1/c. Sorting such a triple gives a<b<c, and the
relation is exactly a(b+c)=bc. The Lean theorem `unit_fraction_equivalence`
proves this equivalence over exact core `Rat`; `admissible_iff_rat` transfers
the whole admissibility condition, and `rat_plateau_732` states the plateau
directly with rational unit fractions. This bridge uses no native checker.

**Lean theorem proved:** f(732)=f(731), expressed without assuming either numerical
value. Every admissible subset of [1,732] can be replaced by an admissible subset
of [1,731] of at least the same cardinality. The reverse implication is immediate.

**Numerical consequence:** OEIS A390395's b-file ends with f(731)=606. Combining
that external published computational baseline with our formal transition yields
f(732)=606. This file does not claim the baseline was formalized in Lean. The
independent integer verifier checks an explicit 606-element witness in [1,732].

The proof isolates G={122,183,244,366,732}. The only forbidden triples meeting G
are {122,183,366}, {183,244,732}, and {244,366,732}. Thus any admissible set contains
at most three members of G. Replace its intersection with G by {122,183,244}.
The new set stays admissible, has at least as many elements, and avoids732.

## Files and verification

- `Plateau302.lean`: complete semantic theorem for arbitrary Boolean membership
  functions on the natural numbers; domain coverage and absence of duplicates
  proved; cardinality and all support/reciprocal-equation conditions proved.
- `witness302.json`: exact 606-element witness, represented both as a set and its
  126-element complement. Solver status in this exploratory JSON is historical
  metadata, not the formal certificate.
- `verify302.py`: dependency-free independent integer check of the witness and
  isolation; run with `python verify302.py`.
- Discovery used an exploratory HiGHS MILP. Its numerical upper bound is not used as the formal proof; the included files reproduce the mathematical verification independently.

Compiled successfully with Lean 4.33.1. The current `plateau_732` and
`exact_maximum_transfer` depend only on `propext`, `Classical.choice`, and
`Quot.sound`. `KernelIsolation.lean` reconstructs the third denominator as
`a*b/(b-a)` and checks three finite tables with `decide +kernel`.
Those closed table certificates have no axioms. There are no `sorry` declarations,
user axioms, native-checker axioms, or hidden numerical assumptions in the current
proof. The initially published native `bv_decide` version remains in Git history;
this revision replaces its proof mechanism without changing the theorem.

## Sources and priority limits

Checked 2026-09-07:

- https://oeis.org/A390395 defines the function and links the table through731.
- https://oeis.org/A390395/b390395.txt ends at `731 606`; the b-file credits
  Sharvil Kesarwani and earlier terms to Chai Wah Wu.
- https://www.erdosproblems.com/302 is the parent problem; direct fetch was403,
  so no claim here is based on a newly read current forum page.
- Search queries included exact combinations of `A390395`, `732`, `606`,
  `erdosproblems.com/302`, and `site:x.com`. No indexed earlier732 result was
  found. This does not prove universal priority or rule out Twitter/unindexed work.
- The local full VibeMathed dataset contained no match for the A390395 identifier
  or the explicit parent-problem URL in this agent's query. Root performed the
  wider catalog review.

The plateau mechanism may be an instance of a known large-prime-component rule.
The appropriate novelty claim is a candidate extension of the published finite
table, pending source/maintainer review, not a newly solved classical conjecture.
The original asymptotic problem remains open. No prize eligibility established.

## Process and inference checks

11. Process integrity: current primary OEIS table read, stale A390394(39) candidate
rejected, exact integer witness independently verified, actual Lean compiler used,
and trust assumptions printed. Gap: inaccessible current problem forum and
incomplete universal priority search.

12. Inference robustness: the structural plateau does not depend on floating-point
MILP or the606 baseline. The numerical606 conclusion is conditional on the
published731 baseline; novelty is provisional. Discovery of a prior component
rule or unpublished/obscure732 computation changes the priority claim, not the
validity of the plateau theorem.
