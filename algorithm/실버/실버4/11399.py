N = int(input())
l = sorted(list(map(int, input().split())))

total = 0
for i in range(len(l)):
    total += sum(l[:i + 1])
print(total)