w, h = map(int, input().split())
mod = 100000
dp = [[[[0] * 2 for _ in range(2)] for _ in range(100)] for _ in range(100)]

for i in range(1, h):
    dp[i][0][0][0] = 1
for i in range(1, w):
    dp[0][i][0][1] = 1

for i in range(1, h):
    for j in range(1, w):
        dp[i][j][0][0] = (dp[i-1][j][0][0] + dp[i-1][j][1][0]) % mod
        dp[i][j][0][1] = (dp[i][j-1][0][1] + dp[i][j-1][1][1]) % mod
        dp[i][j][1][0] = (dp[i-1][j][0][1]) % mod
        dp[i][j][1][1] = (dp[i][j-1][0][0]) % mod

print((dp[h-1][w-1][0][0] + dp[h-1][w-1][1][0] + dp[h-1][w-1][0][1] + dp[h-1][w-1][1][1]) % mod)