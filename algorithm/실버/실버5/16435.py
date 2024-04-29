import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
h = list(map(int, sys.stdin.readline().rstrip().split()))

h.sort()

idx = len(h)
caneat = -1

while(caneat != 0):
    for index in range(len(h)):
        if L < h[index]:
            idx = index
            break
    caneat = len(h[:idx])
    h = h[idx:]
    L += caneat
print(L)