from itertools import permutations

N, M = map(int, input().split())

l = list(map(int, input().split()))

c = sorted(list(tuple(s) for s in set(permutations(l, M))))
for x in c:
    print(*x)