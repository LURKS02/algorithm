N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, depth, visited):
    if depth == 4:
        return True

    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, depth + 1, visited):
                return True
    visited[node] = False
    return False

for i in range(N):
    visited = [False] * N
    if dfs(i, 0, visited):
        print(1)
        exit(0)

print(0)
