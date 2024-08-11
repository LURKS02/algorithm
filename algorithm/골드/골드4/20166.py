from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(10**9)
input = stdin.readline

N, M, K = map(int, input().rstrip().split())
matrix = [list(input().rstrip()) for _ in range(N)]

favoriteDict = dict()

def bfs(startX, startY):
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, 1, -1, 0, 1, -1]

    deq = deque()
    deq.append((startX, startY, matrix[startX][startY]))

    while deq:
        x, y, string = deq.popleft()

        if string not in favoriteDict:
            favoriteDict[string] = 1
        else:
            favoriteDict[string] += 1

        if len(string) >= 5:
            continue

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if nx == N:
                nx = 0
            elif nx == -1:
                nx = N-1

            if ny == M:
                ny = 0
            elif ny == -1:
                ny = M-1

            deq.append((nx, ny, string + matrix[nx][ny]))

ansList = []

for i in range(N):
    for j in range(M):
        bfs(i, j)

for _ in range(K):
    favorite = input().rstrip()
    if favorite in favoriteDict:
        ansList.append(favoriteDict[favorite])
    else:
        ansList.append(0)

for ans in ansList:
    print(ans)