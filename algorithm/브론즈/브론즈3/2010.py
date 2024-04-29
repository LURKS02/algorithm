import sys

N = int(sys.stdin.readline().strip())

total = 0

for i in range(N):
    n = int(sys.stdin.readline().strip())
    total += n - 1

print(total + 1)