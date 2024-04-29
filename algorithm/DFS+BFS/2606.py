import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

visited = [False] * (N + 1)

graph = {i: [] for i in range(1, N + 1)}

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

total = -1
def dfs(graph, v, visited):
    visited[v] = True
    global total
    total += 1
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

dfs(graph, 1, visited)

print(total)
