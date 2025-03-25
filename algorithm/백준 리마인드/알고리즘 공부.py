import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
K = list(map(int, input().split()))

heap = []
for i in range(len(K)):
    heapq.heappush(heap, (K[i], i+1))

R = int(input())

selected = set()
graph = defaultdict(list)

for _ in range(R):
    A, B, D = map(int, input().split())

    graph[A].append((B, D))

maxCost = -float('inf')
haveToMake = 0

while haveToMake < M and heap:
    cost, idx = heapq.heappop(heap)
    if idx in selected:
        continue

    haveToMake += 1
    maxCost = max(maxCost, cost)
    selected.add(idx)

    for neighbor, discount in graph[idx]:
        K[neighbor-1] -= discount
        heapq.heappush(heap, (K[neighbor-1], neighbor))

print(maxCost)