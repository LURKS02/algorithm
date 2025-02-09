import sys
import heapq
from collections import defaultdict

N, M, K = map(int, sys.stdin.readline().split())

graph = defaultdict(list)

for _ in range(M):
    A, B, time = map(int, sys.stdin.readline().split())
    graph[A].append((B, time))
    graph[B].append((A, time))

heap = []
heapq.heappush(heap, (0, K, 1))
cost = [[float('inf')] * (K+1) for _ in range(N+1)]
for i in range(K+1):
    cost[1][i] = 0

while heap:
    totalCost, chance, node = heapq.heappop(heap)

    if cost[node][chance] < totalCost:
        continue

    for neighbor, val in graph[node]:
        if chance > 0:
            if cost[neighbor][chance-1] > totalCost:
                cost[neighbor][chance-1] = totalCost
                heapq.heappush(heap, (totalCost, chance-1, neighbor))
        if cost[neighbor][chance] > totalCost + val:
            cost[neighbor][chance] = totalCost + val
            heapq.heappush(heap, (totalCost + val, chance, neighbor))

print(min(cost[N]))