# Proposed A390395 extension — not yet submitted

Suggested additional b-file lines (pending OEIS contributor-account approval):

```text
732 606
733 607
734 608
```

This uses the currently published a(731)=606. We prove a(732)=a(731) without assuming that numerical value. The isolated component {122,183,244,366,732} has exactly three forbidden triples: {122,183,366}, {183,244,732}, and {244,366,732}. Its independence number is 3, unchanged on deleting 732. The complementary component is unchanged. Hence a(732)=a(731).

The adjacent vertices 733 and 734 participate in no forbidden triple on {1,...,734}. The Lean extension proves this arithmetic fact for every ordered positive reciprocal triple, and then proves exact maximum transfers a(733)=a(732)+1 and a(734)=a(732)+2, including both lower and upper bounds. Explicit witnesses of sizes 607 and 608 are checked by exact integer enumeration. These are bundled consequences of the same finite contribution, not three separate conjecture-resolution claims.

A Lean 4.33.1 proof, explicit witnesses, exact Python verifiers, and full trust disclosure are available at https://github.com/Sodelin/oldest-conjecture- . See the verification record for the exact version and its trust assumptions. The existing upper bound at 731 remains external; it is not claimed as a newly formalized result.

We would appreciate a priority check: this component argument may be known or folklore, and no claim of first discovery is made. The associated general large-prime identity is proved in prose in `general-identity.md` and is not part of the Lean certification.

AI disclosure: initiated by the Sodelin project owner; argument and artifacts developed by an OpenAI ChatGPT/Codex assistant, with separate AI checks and no human expert endorsement yet.
