n = int(input())
l = list(map(int, input().split()))

l.sort()

sum = 0
for i in range(len(l) - 1):
    sum += l[i]
print(sum)