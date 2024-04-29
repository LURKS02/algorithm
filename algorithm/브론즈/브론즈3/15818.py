N, M = map(int, input().split())
l = list(map(int, input().split()))
total = 1
for num in l:
    total *= num

print(total % M)