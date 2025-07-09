import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
INF = sys.maxsize

graph = [[INF for i in range(N+1)] for i in range(N+1)]

for i in range(M):
    a, b, val = map(int, input().split())
    graph[a][b] = val

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            bigger = graph[i][k] if graph[i][k] > graph[k][j] else graph[k][j]
            graph[i][j] = bigger if graph[i][j] > bigger else graph[i][j]

for tc in range(T):
    a, b = map(int, input().split())
    if graph[a][b] != INF:
        print(graph[a][b])
    else:
        print(-1)