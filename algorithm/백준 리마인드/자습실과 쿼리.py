import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())

leftWalls = [0] * (N+2)
rightWalls = [0] * (N+2)

for _ in range(M):
    W, D = map(int, input().split())
    leftWalls[W] = D
    rightWalls[W] = D

for i in range(1, N+1):
    leftWalls[i] += leftWalls[i-1]
    rightWalls[N-i] += rightWalls[N-i+1]

leftBreak = 0
rightBreak = N+1

for i in range(Q):
    P = int(input())

    left = max(leftWalls[P]-leftWalls[leftBreak], 0)
    right = max(rightWalls[P]-rightWalls[rightBreak], 0)

    if left < right:
        leftBreak = max(P, leftBreak)
        print(left)
    elif left > right:
        rightBreak = min(P, rightBreak)
        print(right)
    else:
        if N - P > P - 1:
            leftBreak = max(P, leftBreak)
            print(left)
        elif N - P < P - 1:
            rightBreak = min(P, rightBreak)
            print(right)
        else:
            leftBreak = max(P, leftBreak)
            print(left)