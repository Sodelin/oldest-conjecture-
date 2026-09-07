# P302 / S:gap:302:0671dbe2: structural plateau at 732 for review

The atlas records A390395(732) between 606 and 607. We have a compiled Lean 4.33.1 proof of the structural identity **f(732)=f(731)**, plus a checked 606-element witness. Combining the theorem with the atlas/OEIS external baseline f(731)=606 selects 606 for the next cell.

Source, pinned to the published proof commit: https://github.com/Sodelin/oldest-conjecture-/tree/0d2885f58c5fe6eee8703cdee83a843a1594a7ea

Passing build, leanchecker and exact Python check: https://github.com/Sodelin/oldest-conjecture-/actions/runs/34127973633

The component G={122,183,244,366,732} is isolated. Its only reciprocal-triple edges are {122,183,366}, {183,244,732}, and {244,366,732}. At most three members of G can be selected. Replacing a selection in G by {122,183,244} preserves admissibility, does not reduce its size, and removes 732. This proves the plateau without assuming a numerical extremum.

The Lean exports `plateau_732`, `rat_plateau_732`, and `exact_maximum_transfer` include arbitrary-set support, cardinality coverage/nodup, and the exact rational-equation bridge. The finite isolation lemma uses the default native `bv_decide` LRAT checker, so its dependencies include a generated native checker axiom as well as `propext`, `Classical.choice`, and `Quot.sound`. There is no `sorry` or user axiom; this is not a kernel-only certificate. The 731 upper baseline is external and remains an explicit premise of the numerical transfer.

This is a **candidate finite contribution**, not a resolution of the asymptotic Erdős problem or a first-discovery claim. A general large-prime recurrence is proved separately in prose and may be folklore. Searches of the current OEIS table, relevant GitHub notes and issue #152, VibeMathed, papers, and indexed X posts found no earlier explicit 732 result; direct live Twitter and the current problem forum were not accessible.

Would you check priority and whether this is suitable evidence for the existing P302 finite gap? I have not modified atlas ledgers or claimed compliance with the atlas's internal certificate-contract format. The standalone verifier runs with `python3 -I verify302.py` and the full build with `lake build`.

AI disclosure: the Sodelin project owner initiated and directed the research; an OpenAI ChatGPT/Codex assistant developed the argument and artifacts, with separate AI reviews. No human expert endorsement has yet been obtained.
