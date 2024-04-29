import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

s = set()
for _ in range(N):
    str = sys.stdin.readline().rstrip()
    s.add(str)

sum = 0
for _ in range(M):
    if sys.stdin.readline().rstrip() in s:
        sum += 1

print(sum)