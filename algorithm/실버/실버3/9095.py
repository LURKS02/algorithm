dp = [0] * 12
dp[0] = 1
dp[1] = 1
dp[2] = 2

T = int(input())

for _ in range(T):
    n = int(input())
    if n <= 2:
        print(dp[n])
    else:
        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        print(dp[n])
