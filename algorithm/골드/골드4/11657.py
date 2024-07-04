import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
edges = []
cost = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bellman_ford(start):
    cost[start] = 0

    for i in range(1, N+1):
        for j in range(M):
            now, next, c = edges[j]

            if cost[now] != INF and cost[next] > cost[now] + c:
                cost[next] = cost[now] + c
                if i == N:
                    return True

    return False

negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if cost[i] == INF:
            print(-1)
        else:
            print(cost[i])