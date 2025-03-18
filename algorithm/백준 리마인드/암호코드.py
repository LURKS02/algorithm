password = list(map(int, list(input())))
N = len(password)
MOD = 1000000

dp = [0 for _ in range(N+1)]
dp[0] = 1

for i in range(1, N+1):
    if 1 <= password[i-1] <= 9:
        dp[i] = (dp[i] + dp[i-1]) % MOD
    if i >= 2 and 10 <= password[i-2] * 10 + password[i-1] <= 26:
        dp[i] = (dp[i] + dp[i-2]) % MOD

print(dp[N])
