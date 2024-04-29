N = int(input())

P = [0] + list(map(int, input().split()))

dp = [0 for _ in range(N+1)]

for i in range(1, N + 1):
    dp[i] = max(dp[k] + P[i-k] for k in range(0, i))

print(dp[N])