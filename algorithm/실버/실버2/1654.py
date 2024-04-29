import sys

K, N = map(int, sys.stdin.readline().rstrip().split())

l = []
for _ in range(K):
    l.append(int(sys.stdin.readline().rstrip()))

top = max(l)
bottom = 1

while(bottom <= top):
    mid = (top + bottom) // 2
    s = sum([r // mid for r in l])
    if s >= N:
        bottom = mid + 1
    else:
        top = mid - 1

print(top)
