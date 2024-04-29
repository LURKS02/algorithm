import sys

N = int(sys.stdin.readline().rstrip())
roadlist = list(map(int, sys.stdin.readline().rstrip().split()))
oillist = list(map(int, sys.stdin.readline().rstrip().split()))
oillist.pop()

minoil = 1000000001

count = 0
for i in range(N - 1):
    if oillist[i] > minoil:
        count += roadlist[i] * minoil
    else:
        minoil = oillist[i]
        count += roadlist[i] * minoil

print(count)