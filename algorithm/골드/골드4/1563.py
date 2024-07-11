MAX = 1000
MOD = 1000000

N = int(input())

# N일 동안, 지각 횟수, 연속 결석 횟수
dp = [[[0] * 3 for _ in range(2)] for _ in range(MAX+1)]
dp[1][0][0] = 1
dp[1][0][1] = 1
dp[1][1][0] = 1

for n in range(2, MAX+1):
    dp[n][0][0] = (dp[n-1][0][0] + dp[n-1][0][1] + dp[n-1][0][2]) % MOD
    dp[n][0][1] = dp[n-1][0][0]
    dp[n][0][2] = dp[n-1][0][1]
    dp[n][1][0] = (dp[n-1][1][0] + dp[n-1][1][1] + dp[n-1][1][2] + dp[n-1][0][0] + dp[n-1][0][1] + dp[n-1][0][2]) % MOD
    dp[n][1][1] = dp[n-1][1][0]
    dp[n][1][2] = dp[n-1][1][1]

print((dp[N][1][0] + dp[N][1][1] + dp[N][1][2] + dp[N][0][0] + dp[N][0][1] + dp[N][0][2]) % MOD)