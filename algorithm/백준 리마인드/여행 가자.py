N = int(input())
M = int(input())

graph = []

for _ in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

route = list(map(int, input().split()))

cost = [[float('inf')] * N for _ in range(N)]

for i in range(N):
    cost[i][i] = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cost[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(len(route)-1):
    if cost[route[i]-1][route[i+1]-1] != float('inf'):
        continue
    else:
        print('NO')
        exit(0)

print('YES')