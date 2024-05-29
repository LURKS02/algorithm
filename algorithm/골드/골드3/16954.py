import sys
input = sys.stdin.readline
from collections import deque

board = [input().rstrip() for _ in range(8)]
wall = set()
answer = 0

for i in range(8):
    for j in range(8):
        if board[i][j] == '#':
            wall.add((i, j))

directions = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

visited = set()

deq = deque()
deq.append((7, 0))

while deq:
    for _ in range(len(deq)):
        x, y = deq.popleft()

        if (x, y) in wall:
            continue

        if x == 0 and y == 7:
            answer = 1
            break

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < 8 and 0 <= ny < 8 and not (nx, ny) in visited and not (nx, ny) in wall:
                visited.add((nx, ny))
                deq.append((nx, ny))

    if wall:
        visited = set()

    nextWall = set()
    for x, y in wall:
        if x < 7:
            nextWall.add((x+1, y))

    wall = nextWall

print(answer)