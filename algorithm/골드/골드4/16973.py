from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

walls = []

for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            walls.append((i, j))

def move(r, c):
    deq = deque()
    deq.append((r, c))
    maps[Sr][Sc] = 2

    while deq:
        nowR, nowC = deq.popleft()

        if nowR == Fr and nowC == Fc:
            return maps[Fr][Fc] - 2

        for d in range(4):
            newR = nowR + dr[d]
            newC = nowC + dc[d]

            if newR < 0 or newC < 0 or newR > (N-H) or newC > (M-W) or maps[newR][newC] or not check(newR, newC):
                continue

            deq.append((newR, newC))
            maps[newR][newC] = maps[nowR][nowC] + 1

    return -1

def check(startR, startC):
    minR, maxR = startR, startR + H
    minC, maxC = startC, startC + W

    for (r, c) in walls:
        if minR <= r < maxR and minC <= c < maxC:
            return False

    return True

Sr, Sc, Fr, Fc = Sr-1, Sc-1, Fr-1, Fc-1

print(move(Sr, Sc))