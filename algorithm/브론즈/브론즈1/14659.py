import sys

N = int(sys.stdin.readline().strip())

l = list(map(int, sys.stdin.readline().strip().split()))

now = 0
great = 0

for i in range(len(l)):
    if l[i] > now:
        now = l[i]
        count = 0
        for j in range(i + 1, len(l)):
            if now > l[j]:
                count += 1
            else:
                break
        if great < count:
            great = count

print(great)