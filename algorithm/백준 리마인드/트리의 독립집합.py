from collections import defaultdict

N = int(input())
costs = list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = set()
dp = [[0] * 2 for _ in range(N)]
path = [[[] for _ in range(2)] for _ in range(N)]

def dfs(node):
    visited.add(node)
    dp[node][1] += costs[node]
    path[node][1].append(node+1)

    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dfs(neighbor)

            dp[node][0] += max(dp[neighbor][0], dp[neighbor][1])
            dp[node][1] += dp[neighbor][0]

            path[node][1] += result[0]
            if dp[neighbor][0] > dp[neighbor][1]:
                path[node][0] += result[0]
            else:
                path[node][0] += result[1]
    return path[node]

p = dfs(0)
if dp[0][0] > dp[0][1]:
    print(dp[0][0])
    p[0].sort()
    print(*p[0])
else:
    print(dp[0][1])
    p[1].sort()
    print(*p[1])


dfs(1)