import sys
sys.setrecursionlimit(10**9)

from collections import defaultdict, deque

N, M = map(int, input().split())
heights = [0] + list(map(int, input().split()))
loads = set()

dp = [-float('inf')] * (N+1)

for _ in range(M):
    ia, ib = map(int, input().split())
    a, b = heights[ia], heights[ib]

    if a > b:
        loads.add((ib, ia))
    else:
        loads.add((ia, ib))

graph = defaultdict(list)
for a, b in list(loads):
    graph[a].append(b)

def solve(start):
    if dp[start] != -float('inf'):
        return dp[start]

    if not graph[start]:
        return 0

    for neighbor in graph[start]:
        dp[start] = max(dp[start], solve(neighbor) + 1)

    return dp[start]

for i in range(1, len(heights)):
    print(solve(i)+1)


