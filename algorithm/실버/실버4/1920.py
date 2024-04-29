import sys

N = int(sys.stdin.readline().strip())
ansl = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

def findN(n, start, end):
    if start > end:
        return False
    pindex = (start + end) // 2
    pivot = ansl[pindex]
    if pivot == n:
        return True
    elif pivot > n:
        return findN(n, start, pindex - 1)
    else:
        return findN(n, pindex + 1, end)

M = int(sys.stdin.readline().strip())
myl = list(map(int, sys.stdin.readline().rstrip().split()))

for num in myl:
    if findN(num, 0, len(ansl) - 1):
        print(1)
    else:
        print(0)