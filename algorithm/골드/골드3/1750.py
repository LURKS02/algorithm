import sys
import math
MOD = 10000003
input = sys.stdin.readline

N = int(input())
l = [int(input()) for _ in range(N)]
ans = 0

dp = [0] * (max(l) + 1)

for i in range(N):
    for j in range(1, max(l) + 1):
        if dp[j]:
            dp[math.gcd(j, l[i])] += dp[j]
    dp[l[i]] += 1

print(dp[1] % MOD)