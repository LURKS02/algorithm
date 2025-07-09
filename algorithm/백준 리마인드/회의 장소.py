import sys
import bisect
input = sys.stdin.readline

N, Q = map(int, input().split())
X = list(map(int, input().split()))

pf = [0]

for i in range(len(X)):
    pf.append(pf[-1] + X[i])

for _ in range(Q):
    L, R = map(int, input().split())
    leftIndex = bisect.bisect_left(X, L)
    if leftIndex >= len(X):
        print(0)
        continue
    rightIndex = bisect.bisect_right(X, R)
    if rightIndex == 0:
        print(0)
        continue
    rightIndex -= 1

    if leftIndex >= rightIndex:
        print(0)
        continue

    def getValue(start, end, pivot):
        value = 0

        rightEdge = pf[end+1] - pf[pivot+1] - (end - pivot) * X[pivot]
        leftEdge = (pivot - start) * X[pivot] - (pf[pivot] - pf[start])

        return rightEdge + leftEdge


    maxStress = max(getValue(leftIndex, rightIndex, leftIndex), getValue(leftIndex, rightIndex, rightIndex))
    minStress = getValue(leftIndex, rightIndex, (leftIndex+rightIndex) // 2)

    print(maxStress - minStress)