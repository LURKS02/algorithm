import heapq
from collections import deque, defaultdict

N, M = map(int, input().split())
A, B, K, G = map(int, input().split())

loads = list(map(int, input().split()))

graph = defaultdict(list)
g = [[float('inf')] * (N+1) for _ in range(N+1)]

for _ in range(M):
    U, V, L = map(int, input().split())
    graph[U].append((V, L))
    graph[V].append((U, L))
    g[U][V] = L
    g[V][U] = L

block = [[[0, 0]] * (N+1) for _ in range(N+1)]

time = 0
for i in range(len(loads)-1):
    a = loads[i]
    b = loads[i+1]

    block[a][b] = [time, time + g[a][b] - 1]
    block[b][a] = [time, time + g[a][b] - 1]
    time = time + g[a][b]

cost = [float('inf')] * (N+1)
heap = []
heap.append((0, K, A))
cost[A] = 0
while heap:
    c, time, node = heapq.heappop(heap)

    if node == B:
        print(c)
        exit(0)

    for neighbor, value in graph[node]:
        # 국왕이 껴있을 때
        if block[node][neighbor][0] <= time <= block[node][neighbor][1]:
            if c + value < cost[neighbor]:
                cost[neighbor] = c + value
                heapq.heappush(heap, (c + value + block[node][neighbor][1]+1 - time, block[node][neighbor][1] + 1 + value, neighbor))
        else:
            if c + value < cost[neighbor]:
                cost[neighbor] = c + value
                heapq.heappush(heap, (c + value, time + value, neighbor))
