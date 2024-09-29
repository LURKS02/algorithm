N = int(input())
t = list(map(int, input().split()))

dp = [[[[float('inf')] * 10 for _ in range(10)] for _ in range(10)] for _ in range(N+1)]

dp[0][0][0][0] = 0

for i in range(0, N):
    temp = t[i]

    for j in range(10):
        for k in range(10):
            for m in range(10):
                if dp[i][j][k][m] == float('inf'):
                    continue
                dp[i+1][temp][k][m] = min(dp[i+1][temp][k][m], dp[i][j][k][m] + min(abs(j - temp), j + 10 - temp, temp + 10 - j))
                dp[i+1][j][temp][m] = min(dp[i+1][j][temp][m],
                                            dp[i][j][k][m] + min(abs(k - temp), k + 10 - temp, temp + 10 - k))
                dp[i+1][j][k][temp] = min(dp[i+1][j][k][temp],
                                            dp[i][j][k][m] + min(abs(m - temp), m + 10 - temp, temp + 10 - m))

minValue = float('inf')

for i in range(10):
    for j in range(10):
        for k in range(10):
            minValue = min(minValue, dp[N][i][j][k])

print(minValue)