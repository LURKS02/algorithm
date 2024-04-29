from itertools import combinations

N, M = map(int, input().split())
l = list(map(int, input().split()))

c = sorted([list(s) for s in set(tuple(sorted(list(s))) for s in set(combinations(l, M)))])

for r in c:
    print(*r)
