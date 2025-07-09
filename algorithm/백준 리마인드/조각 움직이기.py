from collections import deque
import heapq

board = [list(input()) for _ in range(5)]

spots = set()

for i in range(5):
    for j in range(5):
        if board[i][j] == '*':
            spots.add((i, j))

heap = []
heap.append((0, spots))

visited = [[[[[float('inf')] * (1 << 6 - 1) for _ in range(1 << 6 - 1)] for _ in range(1 << 6 - 1)] for _ in range(1 << 6 - 1)] for _ in range(1 << 6 - 1)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while heap:
    count, s = heapq.heappop(heap)

    tempList = list(s)
    notVisited = s.copy()
    tempMatrix = [["."] * 5 for _ in range(5)]
    for (tx, ty) in tempList:
        tempMatrix[tx][ty] = "*"
    deq = deque()
    deq.append(tempList[0])
    notVisited.remove(tempList[0])

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and tempMatrix[nx][ny] == "*" and (nx, ny) in notVisited:
                notVisited.remove((nx, ny))
                deq.append((nx, ny))

    if len(notVisited) == 0:
        print(count)
        break

    bits = [0, 0, 0, 0, 0]

    for (sx, sy) in s:
        bits[sx] = bits[sx] | 1 << sy

    for (sx, sy) in s:
        for i in range(4):
            nx, ny = sx + dx[i], sy + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in s:
                tempSet = s.copy()
                tempSet.remove((sx, sy))
                tempSet.add((nx, ny))

                bits = [0, 0, 0, 0, 0]

                for (tx, ty) in tempSet:
                    bits[tx] = bits[tx] | 1 << ty

                if visited[bits[0]][bits[1]][bits[2]][bits[3]][bits[4]] > count+1:
                    visited[bits[0]][bits[1]][bits[2]][bits[3]][bits[4]] = count+1
                    heapq.heappush(heap, (count+1, tempSet))

