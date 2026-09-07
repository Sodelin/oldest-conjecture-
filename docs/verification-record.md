# Verification record

## Current kernel-checked revision

The integrated Lean 4.33.1 build now includes `KernelIsolation`, `KernelEndpoints734`, `Plateau302`, and `Extension734`. It compiled successfully; the exact output is in [kernel-build-validation.log](kernel-build-validation.log).

Published proof commit: [`ced445d951ea043fda41b03044192838a838b0f3`](https://github.com/Sodelin/oldest-conjecture-/tree/ced445d951ea043fda41b03044192838a838b0f3). [GitHub Actions run 34129895492](https://github.com/Sodelin/oldest-conjecture-/actions/runs/34129895492), job `proof` (101767229128), completed successfully. The logs confirm `leanchecker` success, all exact witness checks, and a strict audit of 61 declarations with the allowlist `[propext, Classical.choice, Quot.sound]`.

All five closed finite certificates are axiom-free and evaluated with `decide +kernel`. The complete plateau, adjacent maximum transfers, and conditional numerical consequence through 734 have only `propext`, `Classical.choice`, and `Quot.sound`. No native checker or SAT assumption remains in the theorem closure. CI has been updated to run `leanchecker Extension734` and a strict axiom audit rooted at `Extension734`.

The 607- and 608-element witnesses independently pass exact integer enumeration; both bounds have precisely 738 forbidden triples and no triple touches 733 or 734. A separate AI semantic audit checked that the full cardinality counts through 734 once, arbitrary-set support is correct, and the maximum transfers prove upper and lower bounds. No human expert endorsement or universal priority claim is implied.

The external numerical upper bound at 731 remains explicit. Kernel checking removes a formal trust dependency; it does not resolve that external baseline or prove originality.

## Original published revision

Proof source commit: `0d2885f58c5fe6eee8703cdee83a843a1594a7ea`.

Toolchain: Lean 4.33.1, pinned in `lean-toolchain`; no mathlib dependency.

Local compilation and `lake build` succeeded. The independent Python exact checker confirmed a 606-element admissible set, all 738 forbidden triples on [1,732], the isolated five-vertex component, and replacement to a 606-element set on [1,731].

GitHub Actions [run 34127973633](https://github.com/Sodelin/oldest-conjecture-/actions/runs/34127973633), job `proof` (101761034826), completed successfully. The official-toolchain action built `Plateau302`, ran `leanchecker Plateau302`, and succeeded. Separate steps printed the formal dependencies and reran the exact Python verifier successfully. This CI run used the official Lean installation without the local executable-location shim.

Printed dependencies of the plateau and maximum-transfer theorems:

```text
propext
Classical.choice
Quot.sound
isolated_gadget._native.bv_decide.ax_1_5
```

The final item is Lean's native-evaluated certificate-checker axiom. The workflow prints it explicitly and does not claim that a strict three-logical-axiom audit passed. The rational-equivalence and domain/cardinality audit lemmas use only the three ordinary logical axioms.

Separate assistant instances checked the argument and statement independently of the authoring instance. This is an AI review, not human expert endorsement. The proof makes no numerical assumption in the plateau theorem; `exact_maximum_transfer` exposes the 731 baseline as its hypothesis. The general large-prime theorem in prose is outside the scope of the Lean build.

The historical native-checker statements above describe the original commit only. The current revision replaces those checks as described at the top of this record. The mathematical artifact is reproducible; novelty and historical priority remain unverified.
