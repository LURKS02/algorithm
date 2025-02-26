import sys

N, M = map(int, sys.stdin.readline().split())

items = []
bags = []

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    items.append((W, V))

for _ in range(M):
    bag = int(sys.stdin.readline())
    bags.append(bag)

maxBag = max(bags)

dp = [0] * (maxBag + 1)

for w, v in items:
    for i in range(maxBag, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

maxBagNumber = 0
maxBagPercent = -1.0

for i in range(len(bags)):
    percent = dp[bags[i]] / bags[i]
    if percent > maxBagPercent:
        maxBagPercent = percent
        maxBagNumber = i + 1

print(maxBagNumber)