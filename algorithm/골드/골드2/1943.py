for _ in range(3):
    N = int(input())
    coins = []
    totalMoney = 0

    for _ in range(N):
        value, count = map(int, input().split())
        coins.append((value, count))
        totalMoney += value * count

    if totalMoney % 2 == 1:
        print(0)
        continue

    totalMoney = totalMoney // 2

    # dp = [경우의 수] * 만들 수 있는 돈
    dp = [False] * (totalMoney + 1)
    dp[0] = True

    for val, count in coins:
        for money in range(totalMoney, val-1, -1):
            if dp[money - val]:
                for cnt in range(count):
                    if money + val*cnt <= totalMoney:
                        dp[money + val*cnt] = True

    print(1 if dp[totalMoney] else 0)
