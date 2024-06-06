import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, cost = map(int, input().rstrip().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

def dijkstra(start):
    heap = []
    heap.append((0, start))
    costList = [-float('inf') for _ in range(N+1)]
    costList[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)
        cost = -cost

        if cost < costList[node]:
            continue

        for neighbor, value in graph[node]:
            newValue = cost + value
            if newValue > costList[neighbor] and costList[neighbor] == -float('inf'):
                costList[neighbor] = newValue
                heapq.heappush(heap, (-newValue, neighbor))

    maxValue = max(costList[1:])
    return maxValue, costList.index(maxValue)

_, maxIndex = dijkstra(1)
answer, _ = dijkstra(maxIndex)
print(answer)