from collections import defaultdict
import heapq

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

s = set()

heap = []
heap.append((1, 0))
edges = defaultdict(int)
cost = [float('inf') for _ in range(N+1)]
cost[1] = 0

while heap:
    node, total = heapq.heappop(heap)

    for neighbor, c in graph[node]:
        newTotal = total + c
        if newTotal < cost[neighbor]:
            cost[neighbor] = newTotal
            edges[neighbor] = node
            heapq.heappush(heap, (neighbor,newTotal))

answer = []

for key in edges:
    if (key, edges[key]) not in answer and (edges[key], key) not in answer:
        answer.append((key, edges[key]))

print(len(answer))
for (a, b) in answer:
    print(a, b)