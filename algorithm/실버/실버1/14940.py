import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

startx, starty = -1, -1

matrix = []

ans = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    new = list(map(int, input().split()))
    if 2 in new:
        startx, starty = i, new.index(2)
    matrix.append(new)

def bfs():
    deq = deque()
    count = 0

    deq.append((startx, starty, count))

    while deq:
        currentX, currentY, currentCount = deq.popleft()

        if currentX >= 0 and currentY >= 0 and currentX < n and currentY < m and ans[currentX][currentY] == -1 and matrix[currentX][currentY] != 0:
            ans[currentX][currentY] = currentCount

            deq.append((currentX - 1, currentY, currentCount + 1))
            deq.append((currentX + 1, currentY, currentCount + 1))
            deq.append((currentX, currentY - 1, currentCount + 1))
            deq.append((currentX, currentY + 1, currentCount + 1))

bfs()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            ans[i][j] = 0

for i in range(n):
    print(*ans[i])

