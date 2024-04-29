import sys
from itertools import combinations
input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

arr1 = arr[:N//2]
arr2 = arr[N//2:]

subsumA = []
subsumB = []

for i in range(len(arr1) + 1):
    combA = combinations(arr1, i)

    for comb in combA:
        subsumA.append(sum(comb))

for i in range(len(arr2) + 1):
    combB = combinations(arr2, i)

    for comb in combB:
        subsumB.append(sum(comb))

subsumA.sort()
ans = 0

for elementB in subsumB:
    if elementB > C:
        continue

    start = 0
    end = len(subsumA) - 1

    while start <= end:
        mid = (start + end) // 2

        if subsumA[mid] + elementB > C:
            end = mid - 1
        else:
            start = mid + 1

    ans += end + 1

print(ans)