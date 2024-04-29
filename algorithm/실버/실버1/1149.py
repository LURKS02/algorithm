import sys

input = sys.stdin.readline

N = int(input().rstrip())

dp = [[0 for _ in range(N)] for _ in range(3)]

for i in range(N):
    R, G, B = map(int, input().rstrip().split())
    if i == 0:
        dp[0][0] = R
        dp[1][0] = G
        dp[2][0] = B

    else:
        dp[0][i] = min(dp[1][i-1] + R, dp[2][i-1] + R)
        dp[1][i] = min(dp[0][i-1] + G, dp[2][i-1] + G)
        dp[2][i] = min(dp[0][i-1] + B, dp[1][i-1] + B)

print(min(dp[0][N-1], dp[1][N-1], dp[2][N-1]))
