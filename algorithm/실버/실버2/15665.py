from itertools import product

N, M = map(int, input().split())
l = list(map(int, input().split()))
s = set(l)

p = sorted(list(list(p) for p in product(s, repeat=M)))
for c in p:
    print(*c)