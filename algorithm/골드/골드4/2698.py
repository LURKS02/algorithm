T = int(input())

for _ in range(T):
    n, k = map(int, input().split())

    dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(n+1)]

    dp[1][0][0] = 1
    dp[1][0][1] = 1

    for i in range(2, n+1):
        for j in range(k+1):
            dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
            dp[i][j][1] = dp[i-1][j][0]
            if j > 0:
                dp[i][j][1] += dp[i-1][j-1][1]

    print(dp[n][k][0] + dp[n][k][1])