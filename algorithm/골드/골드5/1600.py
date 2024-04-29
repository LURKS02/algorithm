from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

kdx = [2, 2, 1, 1, -2, -2, -1, -1]
kdy = [-1, 1, 2, -2, 1, -1, 2, -2]

def bfs(grid, W, H, K):
    deq = deque()
    count = [[[0 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]

    kCount = K

    deq.append((0, 0, kCount))

    while(deq):
        x, y, kCnt = deq.popleft()

        if x == W - 1 and y == H - 1:
            return count[y][x][kCnt]

        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]

            if 0 <= newX < W and 0 <= newY < H and count[newY][newX][kCnt] == 0 and grid[newY][newX] != 1:
                deq.append((newX, newY, kCnt))
                count[newY][newX][kCnt] = count[y][x][kCnt] + 1

        if kCnt > 0:
            for i in range(8):
                newX = x + kdx[i]
                newY = y + kdy[i]

                if 0 <= newX < W and 0 <= newY < H and count[newY][newX][kCnt - 1] == 0 and grid[newY][
                    newX] != 1:
                    deq.append((newX, newY, kCnt - 1))
                    count[newY][newX][kCnt - 1] = count[y][x][kCnt] + 1

    return -1


K = int(input())

W, H = map(int, input().split())


grid = []

for _ in range(H):
    grid.append(list(map(int, input().split())))


print(bfs(grid, W, H, K))
