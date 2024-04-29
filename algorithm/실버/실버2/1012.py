import sys
sys.setrecursionlimit(10**7)

T = int(input())

def checkgrid(M, N, x, y, grid):
    if  x < 0 or y < 0 or x >= M or y >= N or grid[y][x] == 0:
        return
    else:
        grid[y][x] = 0
        checkgrid(M, N, x - 1, y, grid)
        checkgrid(M, N, x + 1, y, grid)
        checkgrid(M, N, x, y - 1, grid)
        checkgrid(M, N, x, y + 1, grid)

for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0] * M for i in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        grid[Y][X] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                checkgrid(M, N, j, i, grid)
                count += 1
    print(count)