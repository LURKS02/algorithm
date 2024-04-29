import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().rstrip().split())
    graph[start].append((end, cost))

start, end = map(int, input().rstrip().split())

cost = [float('inf')] * (N+1)
cost[start] = 0
heap = []
heap.append((0, start)) # cost, node

while heap:
    val, node = heapq.heappop(heap)

    if val > cost[node]:
        continue

    for neighbor, value in graph[node]:
        newValue = val + value
        if newValue < cost[neighbor]:
            cost[neighbor] = newValue
            heapq.heappush(heap, (newValue, neighbor))

print(cost[end])