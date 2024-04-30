import heapq

N, K = map(int, input().split())

graph = [[] for _ in range(0, 100001)]

for i in range(0, 100001):
    if i == 0:
        graph[0].append((1, 1))
    elif i == 100000:
        graph[100000].append((99999, 1))
    else:
        graph[i].append((i+1, 1))
        graph[i].append((i-1, 1))

    if i*2 <= 100000 and i != 0:
        graph[i].append((i*2, 0))

# print(graph)

heap = []
heap.append((0, N))
cost = [float('inf')] * 100001
cost[N] = 0

while heap:
    val, position = heapq.heappop(heap)

    if val > cost[position]:
        continue

    if position == K:
        print(val)
        break

    for neighbor, value in graph[position]:
        newValue = value + val
        if newValue < cost[neighbor]:
            cost[neighbor] = newValue
            heapq.heappush(heap, (newValue, neighbor))
