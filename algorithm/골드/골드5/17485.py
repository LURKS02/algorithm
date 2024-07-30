INF = float('inf')
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[[INF] * 3 for _ in range(M)] for _ in range(N)]

for j in range(M):
    dp[0][j] = [matrix[0][j]] * 3

for i in range(1, N):
    for j in range(M):
        if j != 0:
            dp[i][j][2] = matrix[i][j] + min(dp[i-1][j-1][0], dp[i-1][j-1][1])
        if j != M-1:
            dp[i][j][0] = matrix[i][j] + min(dp[i-1][j+1][1], dp[i-1][j+1][2])
        dp[i][j][1] = matrix[i][j] + min(dp[i-1][j][0], dp[i-1][j][2])

minValue = float('inf')
for j in range(M):
    for k in range(3):
        minValue = min(minValue, dp[N-1][j][k])

print(minValue)