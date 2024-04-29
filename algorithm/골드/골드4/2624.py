T = int(input())
k = int(input())
coins = []

for _ in range(k):
    p, n = map(int, input().split())
    coins.append((p, n))

def countCoin(T, coins):
    dp = [0] * (T+1)
    dp[0] = 1

    for coinValue, coinCount in coins:
        for amount in range(T, coinValue - 1, -1):
            for count in range(1, coinCount + 1):
                if amount >= coinValue * count:
                    dp[amount] += dp[amount - coinValue * count]

    return dp[T]

print(countCoin(T, coins))
