import sys

N = int(sys.stdin.readline().rstrip())
l = []

for _ in range(N):
    l.append(int(sys.stdin.readline().rstrip()))

l.sort(reverse=True)
for num in l:
    print(num)