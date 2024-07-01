import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a = a - 1
    b = b - 1

    graph[a].append((b, c))

def digkstra(node):
    heap = []
    cost = [float('inf')] * N
    cost[node] = 0
    heap.append((0, node))

    while heap:
        c, n = heapq.heappop(heap)

        if c > cost[n]:
            continue

        for neighbor, value in graph[n]:
            newCost = c + value
            if newCost < cost[neighbor]:
                cost[neighbor] = newCost
                heapq.heappush(heap, (newCost, neighbor))

    return cost

for i in range(N):
    l = digkstra(i)
    for j in range(N):
        print(l[j] if l[j] != float('inf') else 0, end=" ")
    print()