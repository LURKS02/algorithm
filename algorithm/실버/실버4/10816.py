import sys

N = int(sys.stdin.readline().rstrip())
cardList = list(map(int, sys.stdin.readline().rstrip().split()))

d = {}

for num in cardList:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

M = int(sys.stdin.readline().rstrip())
numList = list(map(int, sys.stdin.readline().rstrip().split()))

for num in numList:
    if num in d:
        print(d[num], end=' ')
    else:
        print(0, end=' ')