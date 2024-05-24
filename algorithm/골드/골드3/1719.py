import heapq

# n = 집하장의 개수 (200)
# m = 집하장간 경로의 개수 (10,000)
n, m = map(int, input().split())

# graph = 집하장 사이의 경로
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

def dijkstra(start):
    heap = []
    heap.append((0, start))
    cost = [float('inf')] * (n+1)
    cost[start] = 0
    prev = [None] * (n+1)

    while heap:
        c, node = heapq.heappop(heap)

        if c > cost[node]:
            continue

        for neighbor, value in graph[node]:
            newValue = c + value
            if newValue < cost[neighbor]:
                cost[neighbor] = newValue
                prev[neighbor] = node
                heapq.heappush(heap, (newValue, neighbor))

    return cost, prev

def reconstructPath(start, end, prev):
    path = []
    step = end
    while step is not None:
        path.append(step)
        step = prev[step]
    path.reverse()
    return path if path[0] == start else []


answer = []
for i in range(1, n+1):
    answer = []
    _, prev = dijkstra(i)
    for j in range(1, n+1):
        if i == j:
            print("- ", end='')
        else:
            path = reconstructPath(i, j, prev)
            print(path[1], end=' ')
    print()