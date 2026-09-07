# Proposed A390395 extension — not yet submitted

Suggested additional b-file line:

```text
732 606
```

This uses the currently published a(731)=606. We prove a(732)=a(731) without assuming that numerical value. The isolated component {122,183,244,366,732} has exactly three forbidden triples: {122,183,366}, {183,244,732}, and {244,366,732}. Its independence number is 3, unchanged on deleting 732. The complementary component is unchanged. Hence a(732)=a(731).

A Lean 4.33.1 proof, explicit 606-element witness, exact Python verifier, and full trust disclosure are available at https://github.com/Sodelin/oldest-conjecture- . The finite isolation step uses Lean's native `bv_decide` LRAT checker. The existing upper bound at 731 remains external; it is not claimed as a newly formalized result.

We would appreciate a priority check: this component argument may be known or folklore, and no claim of first discovery is made. The associated general large-prime identity is proved in prose in `general-identity.md` and is not part of the Lean certification.

AI disclosure: initiated by the Sodelin project owner; argument and artifacts developed by an OpenAI ChatGPT/Codex assistant, with separate AI checks and no human expert endorsement yet.
