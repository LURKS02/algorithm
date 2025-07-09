N = int(input())
MOD = 1000000007

dp = [0] * (N+1)
sumdp = [0] * (N+1)
dp[0] = 1
dp[1] = 2

if N >= 3:
    sumdp[3] = 1
if N >= 4:
    sumdp[4] = 1 + 2

for i in range(2, N+1):
    dp[i] = (dp[i-1] * 2) % MOD + (dp[i-2] * 3) % MOD
    dp[i] = ((sumdp[i] * 2) % MOD + dp[i]) % MOD

    if i+3 <= N:
        sumdp[i+3] = sumdp[i+2]
        sumdp[i+3] += dp[i]

print(dp[N])