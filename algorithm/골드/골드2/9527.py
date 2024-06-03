import sys
import math

sys.setrecursionlimit(10**8)
a, b = map(int, input().split())

def sumF(x):
    if x <= 0:
        return 0

    seung = int(math.log2(x))
    powValue = 2 ** seung
    if powValue == x:
        return seung * x // 2 + 1

    diff = x - powValue
    return sumF(powValue) + diff + sumF(diff)

print(sumF(b) - sumF(a-1))

