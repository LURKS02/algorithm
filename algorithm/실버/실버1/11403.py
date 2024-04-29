N = int(input())

grid = []

def floyd_warshall(grid, N):
    graph = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0:
                graph[i][j] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    return graph

for _ in range(N):
    grid.append(list(map(int, input().split())))

graph = floyd_warshall(grid, N)
for i in range(len(graph)):
    print(*graph[i])
