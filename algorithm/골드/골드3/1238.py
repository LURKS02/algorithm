import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().rstrip().split())
    graph[start].append((end, cost))

def dijkstra(start, end):
    heap = []
    cost = [float('inf')] * (N+1)
    cost[0] = 0
    cost[start] = 0
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

    return cost[end]

print(max(dijkstra(i, X) + dijkstra(X, i) for i in range(1, N+1)))