n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

cases = [0] * (k+1)
cases[0] = 1
for coin in coins:
    for b in range(coin, k+1):
        cases[b] += cases[b-coin]

print(cases[k])