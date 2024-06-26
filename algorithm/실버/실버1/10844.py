N = int(input())

dp = [[-1 for _ in range(10)] for _ in range(N + 1)]

for i in range(10):
    dp[1][i] = 1

dp[1][0] = 0

if N >= 2:
    for i in range(2, N+1):
        for j in range(10):
            if j == 0:
                dp[i][0] = 0
            elif j == 1:
                if i == 2:
                    dp[i][1] = (dp[i-1][2] + 1) % 1000000000
                else:
                    dp[i][1] = (dp[i-1][2] + dp[i-2][1]) % 1000000000
            elif j == 9:
                dp[i][9] = dp[i-1][8] % 1000000000
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000

print(sum(dp[N]) % 1000000000)


