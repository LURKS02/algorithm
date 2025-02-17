N = int(input())
graph = []
for _ in range(N):
    line = input()
    graph.append([int(i) for i in line])

dp = [[0] * (1<<N) for _ in range(N)]
visited = 1

def dfs(node, count, visited):
    if dp[node][visited] != 0:
        return dp[node][visited]

    maxCount = 0
    for neighbor in range(N):N = int(input())
graph = []
for _ in range(N):
    line = input()
    graph.append([int(i) for i in line])

dp = [[0] * (1<<N) for _ in range(N)]
visited = 1

def dfs(node, count, visited):
    if dp[node][visited] != 0:
        return dp[node][visited]

    maxCount = 0
    for neighbor in range(N):
        if not visited & (1 << neighbor) and count <= graph[node][neighbor]:
            newVisited = visited | 1 << neighbor
            maxCount = max(maxCount, dfs(neighbor, graph[node][neighbor], newVisited) + 1)

    dp[node][visited] = maxCount
    return maxCount

print(dfs(0, 0, 1) + 1)
        if not visited & (1 << neighbor) and count <= graph[node][neighbor]:
            newVisited = visited | 1 << neighbor
            maxCount = max(maxCount, dfs(neighbor, graph[node][neighbor], newVisited) + 1)

    dp[node][visited] = maxCount
    return maxCount

print(dfs(0, 0, 1) + 1)