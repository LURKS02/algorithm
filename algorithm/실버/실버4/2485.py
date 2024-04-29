import sys
import math
from functools import reduce

N = int(sys.stdin.readline())

l = []
for _ in range(N):
    l.append(int(sys.stdin.readline()))

rangeset = set()

for i in range(N - 1):
    rangeset.add(l[i+1] - l[i])

gcd = reduce(math.gcd, rangeset)

if gcd < l[0]:
    end = l[-1] - (l[0] - gcd)
elif gcd > l[0]:
    end = l[-1] + (gcd - l[0])
else:
    end = l[-1]
total = end // gcd
print(total - len(l))