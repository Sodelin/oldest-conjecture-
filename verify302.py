"""Independently verify the explicit witness and the isolated-gadget transition.

Run with Python 3.10+; no external dependencies. This is an exact integer checker,
not a replacement for the Lean semantic theorem or a proof of the 731 baseline.
"""
import json
from pathlib import Path
w = json.loads(Path(__file__).with_name('witness302.json').read_text())
S = set(w['set'])
assert w['n'] == 732 and w['size'] == 606
assert len(S) == len(w['set']) == 606 and all(1 <= x <= 732 for x in S)
triples = []
for b in range(1, 733):
    for c in range(b + 1, 733):
        a, remainder = divmod(b * c, b + c)
        if remainder == 0:
            triples.append((a, b, c))
assert len(triples) == 738
assert all(not {a, b, c} <= S for a, b, c in triples)
G = {122, 183, 244, 366, 732}
local = [t for t in triples if set(t) & G]
assert local == [(122, 183, 366), (183, 244, 732), (244, 366, 732)]
from itertools import combinations
assert max(len(q) for r in range(6) for q in combinations(G, r)
           if all(not set(t) <= set(q) for t in local)) == 3
T = (S - G) | {122, 183, 244}
assert len(T) == 606 and max(T) <= 731
assert all(not set(t) <= T for t in triples)
print('Verified: 606-element witness in [1,732], 738 forbidden triples, isolated gadget maximum3.')
print('Verified: replacement gives a 606-element witness in [1,731].')
print('The universal plateau transition is proved in Plateau302.lean; no numerical upper baseline is assumed here.')
