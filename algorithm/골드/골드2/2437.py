N = int(input())

values = list(map(int, input().split()))

# 1 1 2 3 6 7 30
values.sort()
maxWeight = 0

for value in values:
    if value > maxWeight + 1:
        break
    maxWeight += value

print(maxWeight + 1)