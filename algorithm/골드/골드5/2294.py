n, k = map(int, input().split())

coins = set()

for _ in range(n):
    coins.add(int(input()))

coins = sorted(list(coins))

dp = [float('inf') for _ in range(k + 1)]
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        if dp[i - coin] != float('inf'):
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == float('inf'):
    print(-1)

else:
    print(dp[k])