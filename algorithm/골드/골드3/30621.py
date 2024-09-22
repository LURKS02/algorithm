import sys
import bisect
input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

dpT = [0]
dpC = [0]

for i in range(N):
    t, b, c = T[i], B[i], C[i]
    pastT = t - b

    idx = bisect.bisect_left(dpT, pastT) - 1
    if idx <= 0:
        value = max(c, dpC[-1])
    else:
        value = max((dpC[idx] + c), dpC[-1])
    dpT.append(t)
    dpC.append(value)

print(dpC[-1])
