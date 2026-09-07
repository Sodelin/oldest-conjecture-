# Verification record

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

The mathematical artifact is reproducible. Its novelty and historical priority remain unverified.
