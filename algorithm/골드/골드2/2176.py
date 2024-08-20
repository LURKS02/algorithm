from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())

    graph[A].append((B, C))
    graph[B].append((A, C))

cost = [float('inf')] * (N+1)

deq = deque()
deq.append((2, 0))
cost[2] = 0

while deq:
    node, value = deq.popleft()

    for neighbor, val in graph[node]:
        newValue = value + val
        if newValue < cost[neighbor]:
            cost[neighbor] = newValue
            deq.append((neighbor, newValue))

dp = [0] * (N+1)
dp[2] = 1

sortedNodes = sorted(range(1, N+1), key=lambda x: cost[x])

for node in sortedNodes:
    for neighbor, _ in graph[node]:
        if cost[node] < cost[neighbor]:
            dp[neighbor] += dp[node]

print(dp[1])