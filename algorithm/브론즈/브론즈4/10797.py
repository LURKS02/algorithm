n = int(input())
list = list(map(int, input().split()))

total = 0
for i in list:
    if (i == n):
        total += 1

print(total)