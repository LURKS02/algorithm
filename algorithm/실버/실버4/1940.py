import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

l = list(map(int, sys.stdin.readline().rstrip().split()))

s = set(l)

count = 0
for num in l:
    if M - num in s:
        count += 1
print(count // 2)