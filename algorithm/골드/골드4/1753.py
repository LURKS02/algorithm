import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
K = int(input().rstrip())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))

cost = [float('inf')] * (V+1)
cost[K] = 0
heap = []
heap.append((0, K))

while heap:
    val, node = heapq.heappop(heap)

    if val > cost[node]:
        continue

    for neighbor, value in graph[node]:
        newValue = value + val
        if newValue < cost[neighbor]:
            cost[neighbor] = newValue
            heapq.heappush(heap, (newValue, neighbor))

for i in range(1, V+1):
    if cost[i] == float('inf'):
        print("INF")
    else:
        print(cost[i])