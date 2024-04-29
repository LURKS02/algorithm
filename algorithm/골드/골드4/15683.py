N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

directions = {
    1: [[(1, 0)], [(-1, 0)], [(0, -1)], [(0, 1)]],
    2: [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]],
    3: [[(0, -1), (1, 0)], [(1, 0), (0, 1)], [(0, 1), (-1, 0)], [(-1, 0), (0, -1)]],
    4: [[(-1, 0), (0, -1), (1, 0)], [(0, -1), (1, 0), (0, 1)], [(1, 0), (0, 1), (-1, 0)], [(0, 1), (-1, 0), (0, -1)]],
    5: [[(1, 0), (-1, 0), (0, 1), (0, -1)]]
}

cctv = []

for i in range(N):
    for j in range(M):
        if matrix[i][j] != 0 and matrix[i][j] != 6:
            cctv.append((j, i, matrix[i][j]))

minArea = float('inf')

def dfs(index, grid):
    global minArea
    if index == len(cctv):
        count = sum(row.count(0) for row in grid)
        minArea = min(minArea, count)
        return

    x, y, cctvType = cctv[index]
    for dirs in directions[cctvType]:
        tempgrid = [row[:] for row in grid]
        for dx, dy in dirs:
            nx, ny = x, y
            while 0 <= nx < M and 0 <= ny < N and tempgrid[ny][nx] != 6:
                if tempgrid[ny][nx] == 0:
                    tempgrid[ny][nx] = '#'
                nx += dx
                ny += dy
        dfs(index + 1, tempgrid)

dfs(0, matrix)
print(minArea)