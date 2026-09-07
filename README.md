# Old conjecture probes: a finite plateau for Erdős #302

**Proved in Lean 4.33.1:** the reciprocal-triple-free extremal function satisfies

\[
f(732)=f(731).
\]

Here \(f(n)\) is the largest size of a subset of \(\{1,\ldots,n\}\) containing no three distinct numbers satisfying \(1/a=1/b+1/c\).

This is a small finite result connected to Erdős problem #302. It does **not** solve the historical asymptotic problem. Its novelty is **provisional**: our searches found no earlier explicit 732 result, but neither absence from a table nor a search establishes first discovery.

**Publication status:** [public verification passed](https://github.com/Sodelin/oldest-conjecture-/actions/runs/34127973633). The result was submitted to [VibeMathed's review queue](https://vibemathed.com/queue) and [Erdős Frontier Atlas issue #138](https://github.com/techno-optimist/erdos-frontier-atlas/issues/138) on 7 September 2026. Both await review; neither is claimed as acceptance or priority confirmation.

The [published OEIS A390395 table](https://oeis.org/A390395/b390395.txt), checked on 7 September 2026, ends at \(f(731)=606\). Combining that external baseline with the Lean theorem gives the candidate extension **\(f(732)=606\)**. The upper bound at 731 has not been formalized here. An explicit 606-element witness is independently checked with exact integer arithmetic.

## Reproduce

Install the version pinned in `lean-toolchain`, then run:

```sh
lake build
lake env lean Plateau302.lean
python3 verify302.py
```

The main exports are `Erdos302Finite.plateau_732`, `rat_plateau_732`, and `exact_maximum_transfer`. The rational version states the unit-fraction condition directly. Support, domain coverage, duplicate-free counting, and the natural/rational equation bridge are proved.

For this session's unusual local executable-location environment, `scripts/local-lake.sh` accepts `PROBE_LEAN_ROOT` pointing to the extracted official toolchain. It supplies only the configured executable path to Lean's location lookup. Normal GitHub CI uses the official toolchain directly, without this compatibility launcher.

**Trust disclosure:** the isolated-gadget lemma uses `bv_decide`, whose default native LRAT checker introduces one generated native checker axiom, in addition to `propext`, `Classical.choice`, and `Quot.sound`. There are no `sorry` proofs or user-declared axioms. This is not a kernel-only proof. CI runs `leanchecker` and prints the dependencies; it does not present the native checker as one of the three standard logical axioms.

## Why the proof is short

The five denominators \(\{122,183,244,366,732\}\) form an isolated component of the forbidden-triple hypergraph. Every admissible set selects at most three of them. Replacing those selections with \(\{122,183,244\}\) preserves admissibility, does not reduce size, and removes 732.

- [Proof and verification details](RESULT-302.md)
- [General large-prime identity, with a prose proof](docs/general-identity.md) — this generalization is not Lean-formalized here and may be folklore.
- [Prior-work search and priority limits](docs/novelty-record.md)
- [Publication and recognition record](docs/submission-status.md)
- [Follow-on targets and suggested repository names](docs/target-shortlist.md)

The project was initiated by the owner of [Sodelin](https://github.com/Sodelin). OpenAI's ChatGPT/Codex assistant developed the argument, code, formalization, and documentation; separate assistant instances reviewed the semantics and arithmetic. These are AI reviews, not independent human expert reviews. No first-discovery claim is made.

The separate [Egyptian-Fractions-Erdos-295 project](https://github.com/Sodelin/Egyptian-Fractions-Erdos-295) records a verified reproduction of a known construction and unsuccessful searches for an improvement. That work is not a new solution.
