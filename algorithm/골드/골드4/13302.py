import sys
input = sys.stdin.readline
N, K = map(int, input().split())
if K == 0:
    holidays = []
else:
    holidays = list(map(int, input().split()))

coupon = 0
dp = [[float('inf') for _ in range(110)] for _ in range(110)]

dp[0][0] = 0

for i in range(N+1):
    for j in range(40):
        if dp[i][j] == float('inf'):
            continue

        result = dp[i][j]

        if i+1 in holidays:
            dp[i+1][j] = min(result, dp[i+1][j])

        if j >= 3:
            dp[i+1][j-3] = min(dp[i+1][j-3], result)

        dp[i+1][j] = min(result + 10000, dp[i+1][j])
        for k in range(1, 4):
            dp[i+k][j+1] = min(result + 25000, dp[i+k][j+1])
        for k in range(1, 6):
            dp[i+k][j+2] = min(result + 37000, dp[i+k][j+2])

print(min(dp[N]))