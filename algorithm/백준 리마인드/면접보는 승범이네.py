from collections import defaultdict, deque

N, M, K = map(int, input().split())

graph = defaultdict(list)

def dijkstra(points):
    deq = deque()
    cost = [-float('inf')] * (N + 1)
    for point in points:
        deq.append((point, 0))
        cost[point] = 0

    while deq:
        node, val = deq.popleft()

        for neighbor, c in graph[node]:
            if cost[neighbor] < val + c:
                cost[neighbor] = val + c
                deq.append((neighbor, val + c))

    return cost

for _ in range(M):
    U, V, C = map(int, input().split())
    graph[V].append((U, -C))

destinations = list(map(int, input().split()))

costs = dijkstra(destinations)

maxValue = -float('inf')
maxIndex = -1

for i in range(1, len(costs)):
    if -costs[i] > maxValue:
        maxValue = -costs[i]
        maxIndex = i

print(maxIndex)
print(maxValue)