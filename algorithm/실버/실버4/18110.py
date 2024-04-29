
import sys

n = int(sys.stdin.readline())

l = []

if n == 0:
    print(0)
else:
    for _ in range(n):
        l.append(int(sys.stdin.readline()))
    l.sort()

    exception = round(len(l) * 0.15 + 0.0000001)
    grades = l[exception:len(l) - exception]
    print(round((sum(grades) / len(grades)) + 0.0000001))