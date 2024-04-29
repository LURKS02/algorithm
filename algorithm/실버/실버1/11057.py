N = input()

dp = [[0 for _ in range(10)] for _ in range(int(N))]

for i in range(10):
    dp[0][i] = 1

if int(N) > 1:
    for i in range(1, int(N)):
        for j in range(0, 10):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = sum([dp[i-1][k] % 10007 for k in range(0, j+1)])

print(sum(dp[int(N)-1][k] % 10007 for k in range(0, 10)) % 10007)