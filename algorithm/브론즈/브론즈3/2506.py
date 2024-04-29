N = int(input())

l = list(map(int, input().split()))

sum = 0
w = 0
for num in l:
    if num == 1:
        w += 1
        sum += w
    else:
        w = 0
print(sum)