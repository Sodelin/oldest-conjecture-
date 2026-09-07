# A large-prime identity for reciprocal-sum-free sets

## Statement and scope

For an integer \(N\ge0\), let \(f(N)\) be the maximum cardinality of a subset \(A\subseteq\{1,\ldots,N\}\) for which there are no **pairwise distinct** elements \(a,b,c\in A\) satisfying

\[
\frac1a=\frac1b+\frac1c.
\]

In particular, \(f(0)=0\). All denominators are positive integers. The results below are mathematical proofs in prose. **The general theorem is not formalized here.** Its originality has not been established; the observation may be folklore. It does not resolve the asymptotic question in Erdős Problem #302.

**Theorem.** If \(m\ge1\) is an integer and \(p>2m\) is prime, then

\[
f(mp)-f(mp-1)=f(m)-f(m-1).
\]

## Separation lemma

Consider a pairwise distinct solution \((a,b,c)\) with all three denominators in \(\{1,\ldots,mp\}\). We show that either all three denominators are divisible by \(p\), or none are.

Clearing denominators gives

\[
a(b+c)=bc.
\]

If \(p\) divides any one denominator, reduction modulo \(p\) and primality show that it divides at least one other denominator. Suppose, for a contradiction, that exactly two are divisible by \(p\). Write them as \(pu,pv\), where \(1\le u,v\le m\); distinctness gives \(u\ne v\). Denote the remaining denominator by \(z\), with \(p\nmid z\).

If the two multiples of \(p\) occupy the right-hand side of the reciprocal equation, then

\[
\frac1z=\frac1{pu}+\frac1{pv}
\quad\Longrightarrow\quad
p u v=z(u+v).
\]

Hence \(p\mid u+v\), which is impossible because \(0<u+v\le2m<p\).

Otherwise one multiple occupies the left-hand side. Interchanging the two right-hand denominators if necessary, the equation is

\[
\frac1{pu}=\frac1{pv}+\frac1z
\quad\Longrightarrow\quad
z(v-u)=p u v.
\]

Hence \(p\mid v-u\), impossible because \(0<|v-u|<p\). This proves the separation lemma.

## Proof of the theorem

Let \(H_N\) be the hypergraph whose vertices are \(\{1,\ldots,N\}\) and whose edges are the three-element sets that admit a reciprocal equation as above. Then \(f(N)\) is its independence number: the largest size of a vertex set containing no complete edge.

Partition the vertices of \(H_{mp}\) into

\[
M=\{p,2p,\ldots,mp\},
\qquad
R=\{1,\ldots,mp\}\setminus M.
\]

The separation lemma says that every edge is wholly in one part. Scaling denominators by \(p\) preserves the reciprocal equation and pairwise distinctness. Thus the induced hypergraph on \(M\) is isomorphic to \(H_m\).

For a hypergraph with no edges crossing a vertex partition, its independence number is the sum of the two induced independence numbers. Indeed, any independent set restricts to independent sets in both parts, giving the upper bound; conversely, the union of maximum independent sets in the two parts is independent, giving the lower bound.

Writing \(r\) for the independence number of the induced hypergraph on \(R\), we obtain

\[
f(mp)=r+f(m).
\]

Deleting the vertex \(mp\) leaves exactly the same set \(R\), with exactly the same induced edges. The remaining multiples of \(p\) are \(p,2p,\ldots,(m-1)p\), and their induced hypergraph is isomorphic to \(H_{m-1}\). Consequently,

\[
f(mp-1)=r+f(m-1).
\]

Subtracting proves the theorem. This argument also covers \(m=1\), when the latter set of multiples is empty.

## The finite values at 11 and 12

To enumerate all possible edges, order the right-hand denominators as \(b<c\). Positivity then gives \(a<b<c\), and the reciprocal equation is equivalent to

\[
(b-a)(c-a)=a^2.
\]

Put \(d=b-a\) and \(e=c-a\). Thus \(d,e\) are positive integers with \(d<e\), \(de=a^2\), and \(c=a+e\). Since \(d<e\), we have \(e>a\), so \(c>2a\). For \(c\le12\), this restricts \(a\) to \(1,2,3,4,5\). Checking their unequal factor pairs gives:

| \(a\) | Unequal positive factor pairs \((d,e)\), \(d<e\), of \(a^2\) | Pairs with \(a+e\le12\) |
|---|---|---|
| 1 | None | None |
| 2 | \((1,4)\) | \((1,4)\) |
| 3 | \((1,9)\) | \((1,9)\) |
| 4 | \((1,16),(2,8)\) | \((2,8)\) |
| 5 | \((1,25)\) | None |

Therefore the complete edge set of \(H_{12}\) is

\[
\{2,3,6\},\qquad\{3,4,12\},\qquad\{4,6,12\}.
\]

Only the first edge remains in \(H_{11}\), so \(f(11)=10\): one vertex must be removed, and removing 6 suffices.

For \(H_{12}\), the intersection of its three edges is empty, so deleting a single vertex cannot destroy all three edges. Thus \(f(12)\le10\). Deleting 6 and 12 destroys all three, so \(f(12)\ge10\). Hence

\[
f(11)=f(12)=10.
\]

## Application to 732

For every prime \(p>24\), the theorem with \(m=12\) gives

\[
f(12p)=f(12p-1).
\]

In particular, 61 is prime, \(61>24\), and \(12\cdot61=732\), so

\[
\boxed{f(732)=f(731).}
\]

The nonisolated vertices among the multiples of 61 are

\[
\{122,183,244,366,732\},
\]

and their three edges are precisely the 61-fold scalings of the three edges of \(H_{12}\). This explains the five-vertex certificate directly.

The equality proved here does not independently establish a numerical value for \(f(731)\). If the externally tabulated value \(f(731)=606\) is accepted, it yields \(f(732)=606\). A proof of the numerical value must identify that dependency or supply its own certificate for the value at 731.
