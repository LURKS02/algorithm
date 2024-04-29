MOD = 1000000000

N = int(input())

dp = [0] * (N+1)

if N == 1:
    print(0)
else:
    dp[2] = 1

    for i in range(3, N+1):
        dp[i] = (((dp[i-2] + dp[i-1]) % MOD) * (i-1)) % MOD

    print(dp[N])

