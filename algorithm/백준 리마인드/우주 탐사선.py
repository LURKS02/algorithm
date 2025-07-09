N, K = map(int, input().split())

matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)

for k in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

dp = [[float('inf')] * (1 << N) for _ in range(N)]

def dfs(node, visited):
    if visited == (1 << N) - 1:
        return 0

    if dp[node][visited] != float('inf'):
        return dp[node][visited]

    minCost = float('inf')
    for i in range(N):
        if visited & (1 << i) == 0:
            cost = dfs(i, visited | (1 << i)) + matrix[node][i]
            minCost = min(cost, minCost)

    dp[node][visited] = minCost

    return dp[node][visited]

print(dfs(K, 1 << K))