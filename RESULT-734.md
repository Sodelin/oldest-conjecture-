# Finite extensions through734 for Erdős problem302

## Result

Let f(n) be the largest size of a subset of {1,...,n} without distinct
unit-fraction solutions1/a=1/b+1/c. The compiled Lean development proves:

- Given any exact maximum f(732)=k, then f(733)=k+1 and f(734)=k+2.
- Independently, given any exact maximum f(733)=k, then f(734)=k+1.
- With the explicit premise f(731)=606 and the earlier732 plateau,
  these give f(733)=607 and f(734)=608.

The numerical731 baseline is external and is never asserted as an axiom.
These are finite sequence extensions, not a solution to the asymptotic conjecture.
Priority and publication suitability require the parent's current source review;
this subtask makes no independent first-discovery claim.

## Proof and cardinality audit

The stronger arithmetic lemma `no_new_triples` proves that every ordered
positive solution a<b<c<=734 to a(b+c)=bc already has c<=732. Therefore
vertices733 and734 participate in no forbidden triple. Adding each increases
the optimum by exactly1; deleting it decreases any candidate's size by at most1.

The original732 cardinality definition was NOT silently reused as the full
cardinality. `fullCardinal` explicitly adds the733 and734 indicators. Its domain
is `(outside ++ gadget) ++ [733,734]`; `full_domain_membership` proves coverage
of precisely1,...,734 and `full_domain_nodup` proves no duplicates.
`full_cardinal_domain` proves equality with the ordinary filtered-list count.
The imported exact `Rat` equivalence still identifies the integer equation
with the original unit-fraction statement for positive denominators.

## Files

- `Extension734.lean`: imports `Plateau302` and adds the new `Erdos302Extension734` namespace.
- `KernelEndpoints734.lean`: exact nondivisibility certificates checked by the Lean kernel.
- `witness733.json`:607-element exact witness.
- `witness734.json`:608-element exact witness.
- `verify734.py`: dependency-free independent integer verification.
- `docs/kernel-build-validation.log`: successful integrated build with exact axiom reports.

Both witnesses consist of the previously verified606-element witness in[1,732]
plus the new vertices. The verifier enumerates all pairs b<c, checks the equation
using exact `divmod(b*c,b+c)`, finds exactly738 forbidden triples at both bounds,
confirms their largest member is at most732, and checks each witness avoids all.

## Verification and limitations

Lean 4.33.1 compilation exited 0, with no errors, warnings, `sorry`, or user axioms.
The current structural and numerical-transfer theorems depend only on `propext`,
`Classical.choice`, and `Quot.sound`. For each endpoint c in {733,734}, the kernel
checks that b*c is not divisible by b+c for every 0<b<c. A reciprocal triple
would imply that divisibility, so neither endpoint can occur in a triple.
Both closed endpoint certificates use `decide +kernel` and have no axioms.
The earlier experimental native-checker proof has been replaced. No toolchain
or compiler source was changed to obtain this smaller trust dependency.

Reproduce with the pinned official toolchain:

```sh
lake build
lake env lean Extension734.lean
python3 verify734.py
```

The optional local compatibility launcher is documented in the root README.

11. Process integrity: complete semantic transfer compiled, full cardinality domain
proved, both witnesses independently checked. The earlier OEIS source baseline is
explicit; current priority/submission checks remain with the parent task.

12. Inference robustness: the symbolic+1 transitions do not depend on numerical
MILP or an assumed606 value. The607/608 conclusions depend on the externally
published731 baseline. Previously known isolated-vertex arguments could negate
novelty without affecting these formal statements.
