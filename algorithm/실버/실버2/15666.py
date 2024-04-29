from itertools import combinations_with_replacement

N, M = map(int, input().split())
l = list(map(int, input().split()))

p = sorted([list(s) for s in set([tuple(sorted(list(s))) for s in set(combinations_with_replacement(l, M))])])

for l in p:
    print(*l)