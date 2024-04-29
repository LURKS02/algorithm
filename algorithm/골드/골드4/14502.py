from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus_spread(x, y, temp_lab):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                virus_spread(nx, ny, temp_lab)

def safe_area_count(temp_lab):
    count = 0
    for i in range(N):
        count += temp_lab[i].count(0)
    return count

empty_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
max_safe_area = 0

for walls in combinations(empty_spaces, 3):
    temp_lab = deepcopy(lab)
    for x, y in walls:
        temp_lab[x][y] = 1
    for i in range(N):
        for j in range(M):
            if temp_lab[i][j] == 2:
                virus_spread(i, j, temp_lab)

    max_safe_area = max(max_safe_area, safe_area_count(temp_lab))

print(max_safe_area)

