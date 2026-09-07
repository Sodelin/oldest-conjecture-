# Two follow-on targets

Status checked on 7 September 2026. These are research targets, not solved results or predictions of an easy breakthrough. The present repository's selected target takes priority. Repository names below are suggestions; these additional repositories have not been created.

| Target | Historical anchor | Suggested repository | First useful objective |
|---|---|---|---|
| Erdős #686: consecutive-product ratios, especially 4 and 25 | Exact general question appears in Erdős's 1979 paper, p. 78 | `Sodelin/erdos-686-product-ratios` | A new exact witness for an unresolved square, or a proved exclusion covering a previously untreated family of lengths |
| Erdős–Graham #287: gaps in Egyptian fractions | Attributed to their 1980 monograph, p. 33; the weaker predecessor dates to 1932 | `Sodelin/erdos-287-egyptian-gaps` | Extend a verified finite exclusion frontier, or prove a structural case with an explicit statement and checked proof |

## Erdős #686

Does every integer \(N\ge2\) have a representation

\[
N=\frac{(m+1)(m+2)\cdots(m+k)}{(n+1)(n+2)\cdots(n+k)},
\qquad k\ge2,\quad n\ge0,\quad m\ge n+k?
\]

The inequality requires the two blocks to be disjoint. The current [Formal Conjectures statement](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/686.lean) explicitly retains the cases \(N=4\) and \(N=25\) as open. It records all nonsquares as settled and gives the already-known square example \(9=(26\cdot27\cdot28)/(12\cdot13\cdot14)\). Reproducing these is not a new result. The [community AI-contributions register](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems) lists substantial partial work by multiple researchers and systems.

The original general question was read in [Erdős, *Some unconventional problems in number theory*, Acta Math. Acad. Sci. Hungar. 33 (1979), 71–80](https://www.renyi.hu/~p_erdos/1979-23.pdf), p. 78; [DOI metadata](https://doi.org/10.1007/BF01903382) confirms the publication date. A reference to a 1965 survey in that paper does not establish a 1965 origin for this exact question.

**Tractability:** an integer witness is cheap to verify but may be very difficult to find. Negative results require covering every permitted \(n,m\) in their claimed range. A large unsuccessful search is not a proof of nonexistence. This is suitable for modular sieves and Diophantine subproblems, with a low expectation of resolving the full question in one session.

## Erdős–Graham #287

If distinct integers \(1<n_1<\cdots<n_k\), \(k\ge2\), satisfy

\[
\frac1{n_1}+\cdots+\frac1{n_k}=1,
\]

must some consecutive gap satisfy \(n_{i+1}-n_i\ge3\)? The bound would be sharp: \((2,3,6)\) has sum one and largest gap three. The [current Formal Conjectures file](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/287.lean) classifies the general statement as open. The weaker gap-at-least-two result is known; do not present the open question as an unsolved 1932 conjecture.

The 1980/p.33 attribution is corroborated by [a current problem record](https://api.scinet.pub/p/816b3552-80f9-41ff-bf36-53a8dbaddfed); the original book page was not successfully retrieved at the time of this note. This is an explicit provenance limitation. [Graham's own bibliography](https://math.colgate.edu/~integers/RonGrahamPubs.pdf) confirms the book's 1980 publication.

**Tractability:** this has a finite search for each fixed first denominator, but the number of gap patterns grows quickly. Exact rational arithmetic, divisibility restrictions, and a proved stopping bound can produce a genuine finite theorem. Small cases are already studied: a [July 2026 independent research log](https://lucid.rodeo/erdos/) reports verification through first denominator 12 and explicitly labels that as a reproduction of existing forum work. Any planned extension must check the latest original forum record first. No new finite bound is claimed here.

## What was and was not checked

The current `teorth/erdosproblems` status data label #686 `open` and #287 `falsifiable` (an open problem refutable by one finite witness). Current Formal Conjectures files support the exact statements above. Their open theorems contain `sorry`; a formalized statement is not a verified solution.

The 690-entry VibeMathed snapshot generated on 7 September 2026 had no explicit record matching these problem numbers or their `erdosproblems.com` URLs. Targeted web searches included both spellings of Erdős/Erdos, problem-number phrases, and indexed `x.com` posts. No relevant X resolution announcement was returned. This is limited indexed coverage, not an exhaustive Twitter search or a guarantee of novelty. Direct access to the original Erdős Problems pages failed with HTTP 403, so this note does not certify the newest forum comments.

Before a novelty claim: refresh the original discussion, search papers by the exact proposed theorem, compare every quantified hypothesis and bound, and independently check the proof. VibeMathed absence alone establishes nothing about priority.
