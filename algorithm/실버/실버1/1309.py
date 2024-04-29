N = int(input())

dp = [[0 for _ in range(N)] for _ in range(3)]

dp[0][0] = 1
dp[1][0] = 1
dp[2][0] = 1

for i in range(1, N):
    dp[0][i] = (dp[0][i-1] + dp[1][i-1] + dp[2][i-1]) % 9901
    dp[1][i] = (dp[0][i-1] + dp[2][i-1]) % 9901
    dp[2][i] = (dp[0][i-1] + dp[1][i-1]) % 9901

print((dp[0][N-1] + dp[1][N-1] + dp[2][N-1]) % 9901)