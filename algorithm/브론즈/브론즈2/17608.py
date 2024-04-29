import sys

N = int(sys.stdin.readline().strip())

l = []

for i in range(N):
    l.append(int(sys.stdin.readline().strip()))

start = 0
sum = 0

for i in range(len(l)-1, -1, -1):
    if l[i] > start:
        start = l[i]
        sum += 1

print(sum)
