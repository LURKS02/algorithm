import heapq

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

maxItems = 0

for start in range(1, n+1):
    heap = []
    cost = [float('inf')] * (n+1)
    heap.append((0, start))
    cost[start] = 0

    while heap:
        val, position = heapq.heappop(heap)
        # print(position)
        if cost[position] < val:
            continue

        for neighbor, value in graph[position]:
            newValue = val + value
            # print(newValue)
            if newValue <= m and newValue < cost[neighbor]:
                cost[neighbor] = newValue
                heapq.heappush(heap, (newValue, neighbor))

    # print(cost)
    maxItems = max(maxItems, sum(items[i-1] for i in range(1, n+1) if cost[i] <= m))

print(maxItems)