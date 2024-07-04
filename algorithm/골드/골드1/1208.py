from bisect import bisect_left, bisect_right
from itertools import combinations

def count(subset, target) -> int:
    return bisect_right(subset, target) - bisect_left(subset, target)

def calc_subset(set, subset, n):
    for i in range(1, n+1):
        for comb in combinations(set, i):
            subset.append(sum(comb))

N, S = map(int, input().split())
l = list(map(int, input().split()))

x = []
y = []

for i in range(1, N//2+1):
    for comb in combinations(l[:N//2], i):
        x.append(sum(comb))
for i in range(1, N-N//2+1):
    for comb in combinations(l[N//2:], i):
        y.append(sum(comb))

x.sort()
y.sort()
#
# print(x)
# print(y)

cnt = 0
for i in x:
    cnt += count(y, S - i)

cnt += count(x, S)
cnt += count(y, S)

print(cnt)
