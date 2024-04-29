import sys
sys.setrecursionlimit(10 ** 9)

def dfs(graph, node, parent, parents):
    parents[node] = parent
    for neighbor in graph[node]:
        if parents[neighbor] == 0:
            dfs(graph, neighbor, node, parents)

N = int(input())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = [0] * (N + 1)
dfs(graph, 1, 0, parents)

for i in range(2, N + 1):
    print(parents[i])