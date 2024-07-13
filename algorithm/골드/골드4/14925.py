import sys
input = sys.stdin.readline

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

dp =[[0 for _ in range(N+1)] for _ in range(M+1)]
maxFarm = 0

for i in range(1, M+1):
    for j in range(1, N+1):
        if not matrix[i-1][j-1]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            maxFarm = max(maxFarm, dp[i][j])

# for i in range(1, M+1):
#     print(*dp[i])
print(maxFarm)