from collections import deque

M, N = map(int, input().split())

map = []

for i in range(N):
    map.append(list(int(c) for c in input()))

deq = deque()
deq.append((0, 0))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

breaks = [[float('infinity') for _ in range(M)] for _ in range(N)]
breaks[0][0] = 0

while(deq):
    x, y = deq.popleft()

    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if 0 <= newX < M and 0 <= newY < N:
            cost = breaks[y][x] + map[newY][newX]
            if cost < breaks[newY][newX]:
                breaks[newY][newX] = cost
                if map[newY][newX] == 1:
                    deq.append((newX, newY))
                else:
                    deq.appendleft((newX, newY))

print(breaks[-1][-1])
