import sys
sys.setrecursionlimit(10**9)

N = int(input())
people = [0] + list(map(int, input().split()))
line = []

graph = [[] for _ in range(N+1)]

def dfs(v):
    visited[v] = True
    dp[v][0] = 0
    dp[v][1] = people[v]

    for u in graph[v]:
        if not visited[u]:
            dfs(u)
            dp[v][0] += max(dp[u][0], dp[u][1])
            dp[v][1] += dp[u][0]

for _ in range(N-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

visited = [False] * (N + 1)
dp = [[0, 0] for _ in range(N + 1)]

dfs(1)
print(max(dp[1][0], dp[1][1]))

