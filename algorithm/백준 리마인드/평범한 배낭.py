N, K = map(int, input().split())

items = []

for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

dp = [-float('inf')] * (K+1)
dp[0] = 0

for w, v in items:
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)

print(max(dp))

