import sys
input = sys.stdin.readline

C, D, M = map(int, input().split())

moneys = []

for _ in range(C):
    money = list(map(int, input().split()))
    moneys.append(money)

dp = [0] * 500001

for i in range(D-1):
    dp = [0] * 500001
    for j in range(C):
        value = moneys[j][i+1] - moneys[j][i]
        cost = moneys[j][i]

        if value <= 0: continue

        for k in range(cost, M+1):
            dp[k] = max(dp[k], dp[k-cost] + value)

    M += dp[M]

print(M)