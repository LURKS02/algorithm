import sys

N, M = map(int, sys.stdin.readline().strip().split())

s = []

l1 = list(map(int, sys.stdin.readline().rstrip().split()))
for i in l1:
    s.append(i)

l2 = list(map(int, sys.stdin.readline().rstrip().split()))
for i in l2:
    s.append(i)

L = sorted(s)

for k in L:
    print(k, end=' ')