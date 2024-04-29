import sys

dp = [[-1 for _ in range(100000 + 1)] for _ in range(3)]

dp[0][1] = 1
dp[1][1] = 0
dp[2][1] = 0

dp[0][2] = 0
dp[1][2] = 1
dp[2][2] = 0

dp[0][3] = 1
dp[1][3] = 1
dp[2][3] = 1

for i in range(4, 100000 + 1):
    dp[0][i] = (dp[1][i-1] + dp[2][i-1]) % 1000000009
    dp[1][i] = (dp[0][i-2] + dp[2][i-2]) % 1000000009
    dp[2][i] = (dp[0][i-3] + dp[1][i-3]) % 1000000009

for _ in range(int(input())):
    n = int(input())
    print((dp[0][n] + dp[1][n] + dp[2][n]) % 1000000009)

