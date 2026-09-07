# Prior work and priority record

Search date: 2026-09-07. Claim under review: the finite plateau f(732)=f(731) for the distinct reciprocal-triple extremal function, with a candidate new table term 732 606 conditional on the published value at 731.

## Sources inspected

| Source | What it establishes | Limitation |
|---|---|---|
| [OEIS A390395](https://oeis.org/A390395) and [b-file](https://oeis.org/A390395/b390395.txt) | Function definition and existing values through 731, ending at 606 | An external computational baseline, not a formal upper-bound certificate in this repository |
| [Erdős Frontier Atlas P302](https://github.com/techno-optimist/erdos-frontier-atlas/blob/main/views/graph/P302.md) | Lists the next finite target at 732 with bounds 606–607 | A gap in this research register does not establish universal novelty |
| [Erdős Problems issue #152](https://github.com/teorth/erdosproblems/issues/152) | Relevant prior discussion reviewed by a separate assistant | No claim to have read every historical comment or inaccessible forum thread |
| [Existing AI research note](https://github.com/neelsomani/gpt-erdos/blob/main/data/solutions/302/candidate_solution.md) | Prior asymptotic work and table context | No new 732 theorem or large-prime identity found in the inspected note |
| [Research starts](https://github.com/hjyuh/MathsSTuff/blob/main/erdos/302/research-starts.md) | Prior finite computational work, referring to values through 731 | Search comparison, not a proof of absence elsewhere |
| [VibeMathed dataset](https://vibemathed.com/api/dataset) | The snapshot generated 2026-09-07T13:05:30.828Z contained 690 entries; no relevant entry found | Its catalog is not exhaustive mathematics literature |

The published b-file's displayed program appears to contain a transcription problem (`range(a + 1, n + 1)` before `a` is assigned in that function). We did not treat that listing as an executable upper-bound certificate. The 606 upper baseline is cited as published data and remains an explicit external dependency. Our structural plateau theorem is independent of it.

Additional searches covered OEIS program implementations, GitHub code mentioning A390395, exact combinations of A390395/732/606, the parent problem number and URL, the proposed large-prime recurrence, alphaXiv mathematical-paper search, and indexed X/Twitter queries. A paper on *harmonic triples* was excluded because its equation was 2/a=1/b+1/c, a different problem.

No earlier explicit result at 732 or statement of the recurrence was found. Direct live X coverage was unavailable; indexed searches cannot exclude unindexed posts. Direct requests to the current Erdős Problems forum returned HTTP 403. These are material limitations. AlphaMath was not available as a callable service; alphaXiv and primary-source searches were used, and are not represented as an AlphaMath certification.

## Scope and dates

The 1980 date concerns the parent extremal problem. This finite 732 target must not be advertised as a 46-year-old conjecture solved in 2026. The historical half-density guess has already been refuted by prior work; the full asymptotic extremal problem remains open. The present theorem settles one finite transition.

The general component argument is elementary and may be known or folklore. Appropriate wording is **candidate table extension with a verified structural proof, pending priority review**. GitHub's publication record establishes that these files were public by that timestamp; it does not establish the absence of earlier work.

## Adjacent extension check

The same day's independent source review considered the proposed additional terms 733 607 and 734 608. The current entry and b-file still ended at 731. The [public sequence history](https://oeis.org/history?seq=A390395) showed revision 50, dated 30 November 2025, installing the table through 731; that history response was cached on 1 September 2026, whereas the entry and b-file were crawled on the research date. No later draft appeared in the inspected history. An earlier history discussion mentions 732 hypothetically, without a value or proof.

Targeted searches for A390395 with 733/734/607/608 and indexed X posts found no relevant earlier extension. This establishes only a gap in the inspected public record. The isolated-vertex consequences are elementary and may have been noticed elsewhere. Safe wording is: **three additional terms beyond the inspected published table, derived from proved relations and its published starting value**.

## Process and inference checks

11. Process integrity: separated searches, actual compilation, exact witness verification, an AI semantic audit, and source/status comparison. Gaps: no human expert review, no exhaustive Twitter/forum access, and no formal 731 upper bound.

12. Inference robustness: discovering earlier work would defeat a priority claim, not the theorem. Changing the external 731 baseline would change the numerical extension, not the plateau. The initial native-checker dependency was removed by a subsequent kernel-checked proof revision, with only ordinary logical axioms remaining. The general prose theorem and known asymptotic results are not silently imported as axioms into the finite Lean proof.
