import sys
sys.setrecursionlimit(100000)

def dfs(node, d):
    visited[node] = True
    depth[node] = d

    for neighbor in graph[node]:
        if visited[neighbor]:
            continue
        parent[neighbor] = node
        dfs(neighbor, d + 1)

def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]
    return a

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [0 for i in range(N+1)]
depth = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    print(lca(x, y))

