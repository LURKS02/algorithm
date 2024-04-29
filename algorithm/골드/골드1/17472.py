from collections import deque
import sys
input = sys.stdin.readline

MAX = sys.maxsize

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())

land = []
maps = []

for i in range(N):
    maps.append(list(map(int, input().split())))
    for j in range(M):
        if maps[i][j] == 1:
            land.append((j, i))

def find_land(visited, a, b, num):
    deq = deque()
    deq.append((a, b))

    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and maps[ny][nx] == 1:
                visited[ny][nx] = True
                maps[ny][nx] = num
                start.append((nx, ny, num))
                deq.append((nx, ny))

def find_parent(x):
    if x != island[x]:
        island[x] = find_parent(island[x])
    return island[x]

def union_parent(x, y):
    a, b = find_parent(x), find_parent(y)
    if a > b:
        island[a] = b
    if a < b:
        island[b] = a

def make_straight(nx, ny, dx, dy, num, temp):
    global result
    nx += dx
    ny += dy
    if 0 <= nx < M and 0 <= ny < N:
        if maps[ny][nx] == 0:
            temp[ny][nx] = temp[ny - dy][nx - dx] + 1
            make_straight(nx, ny, dx, dy, num, temp)
        elif temp[ny - dy][nx - dx] >= 2:
            bridge.append((temp[ny - dy][nx - dx], num, maps[ny][nx]))
            return

def make_bridge():
    for x, y, num in start:
        temp = [[0] * M for _ in range(N)]
        for dx, dy in direction:
            make_straight(x, y, dx, dy, num, temp)

def check_all_connected():
    temp = 0
    for i in range(1, landNum + 1):
        if i == 1:
            temp = find_parent(i)
        elif temp != find_parent(i):
            return False

    return True

start = []
visited = [[False] * M for _ in range(N)]
landNum = 1
for i, j in land:
    if not visited[j][i]:
        visited[j][i] = True
        maps[j][i] = landNum
        start.append((i, j, landNum))
        find_land(visited, i, j, landNum)
        landNum += 1
landNum -= 1

direction = [[0, -1], [-1, 0], [0, 1], [1, 0]]
island = [i for i in range(landNum + 1)]

bridge = []
make_bridge()
bridge.sort()

# print(bridge)

result = 0
for len, start, end in bridge:
    if find_parent(start) != find_parent(end):
        result += len
        union_parent(start, end)

if check_all_connected():
    print(result)
else:
    print(-1)