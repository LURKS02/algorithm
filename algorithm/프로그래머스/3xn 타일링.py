def solution(n):
    dp = [0] * (n+1)
    dp[2] = 3
    dp[3] = 0
    dp[4] = 11

    MOD = 1000000007

    for i in range(5, n+1):
        if i % 2 == 0:
            for j in range(i-2, -1, -2):
                if j == i-2:
                    dp[i] += ((dp[j] % MOD) * (dp[2] % MOD)) % MOD
                else:
                    dp[i] += ((dp[j] % MOD) * 2) % MOD
            dp[i] += 2

    return dp[n]

print(solution(6))