
N = int(input())

dp = [float('inf') for i in range(N + 1)]
dp[0] = 0
dp[1] = 1

for i in range(2, N + 1):
    k = 1
    while k*k <= i:
        if dp[i] > 1 + dp[i - k*k]:
            dp[i] = 1 + dp[i - k*k]
        k += 1

print(dp[N])