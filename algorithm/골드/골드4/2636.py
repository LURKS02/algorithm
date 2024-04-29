from collections import deque

N, M = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    deq = deque()
    deq.append((0, 0))
    visited = [[False for _ in range(M)] for _ in range(N)]

    melted = 0

    while deq:
        currentX, currentY = deq.popleft()

        for i in range(4):
            newX, newY = currentX + dx[i], currentY + dy[i]

            if 0 <= newX < M and 0 <= newY < N and not visited[newY][newX]:
                if cheese[newY][newX] == 0:
                    deq.append((newX, newY))
                else:
                    cheese[newY][newX] = 0
                    melted += 1
                visited[newY][newX] = True

    return melted

time = 0
remained = 0

while(True):
    melted = bfs()
    if melted == 0:
        break
    else:
        time += 1
        remained = melted

print(time)
print(remained)
