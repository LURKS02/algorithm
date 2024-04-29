N, K = map(int, input().split())

items = []

for _ in range(N):
    items.append(tuple(map(int, input().split())))

# print(items)

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight, value = items[i-1]
        if weight > j:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight] + value)

print(dp[N][K])
