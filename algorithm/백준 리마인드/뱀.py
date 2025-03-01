from collections import deque, defaultdict

N = int(input())
K = int(input())
apples = set()

for _ in range(K):
    x, y = map(int, input().split())
    apples.add((x-1, y-1))

L = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

directions = dict()

for _ in range(L):
    X, C = input().split()
    if C == "L":
        directions[int(X)] = -1
    else:
        directions[int(X)] = 1

deq = deque()
deq.append((0, 0))
lengthset = set()
lengthset.add((0, 0))
seconds = 0
direction = 0

while True:
    seconds += 1
    cx, cy = deq[-1]

    nx, ny = cx + dx[direction], cy + dy[direction]

    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        break

    if (nx, ny) in lengthset:
        break

    if (nx, ny) in apples:
        apples.remove((nx, ny))
        deq.append((nx, ny))
        lengthset.add((nx, ny))

    else:
        deq.append((nx, ny))
        lengthset.add((nx, ny))
        px, py = deq.popleft()
        lengthset.remove((px, py))

    if seconds in directions:
        direct = directions[seconds]
        direction = (direction + direct + 4) % 4

print(seconds)




