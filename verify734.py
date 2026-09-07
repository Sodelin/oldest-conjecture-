"""Exact independent witness/isolated-vertex verification; no dependencies."""
import json
from pathlib import Path
root = Path(__file__).resolve().parent
for n in (733, 734):
    record = json.loads((root / f'witness{n}.json').read_text())
    S = set(record['set'])
    assert record['n'] == n
    assert len(S) == len(record['set']) == record['size'] == n - 126
    assert all(1 <= x <= n for x in S)
    triples = []
    for b in range(1, n + 1):
        for c in range(b + 1, n + 1):
            a, rem = divmod(b * c, b + c)
            if rem == 0:
                assert 1 <= a < b < c <= n
                triples.append((a,b,c))
    assert len(triples) == 738
    assert all(c <= 732 for a,b,c in triples)
    assert not any({a,b,c} <= S for a,b,c in triples)
    print(f'PASS n={n}: exact{len(S)}-element witness; all738 forbidden triples have largest vertex<=732.')
print('Witnesses prove lower bounds. Lean proves the symbolic maximum transfers;606 at731 is an explicit external baseline.')
