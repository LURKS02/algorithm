from collections import deque
from itertools import combinations

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

answer = 0
appendedSet = set()

def checkAreas(N, M, matrix):
    safeAreas = []
    virusAreas = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                safeAreas.append((i, j))
            elif matrix[i][j] == 2:
                virusAreas.append((i, j))
    return (safeAreas, virusAreas)

def checkSafeArea(N, M, matrix, virus):
    temp_matrix = [row[:] for row in matrix]
    deq = deque(virus)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and temp_matrix[nx][ny] == 0:
                temp_matrix[nx][ny] = 2
                deq.append((nx, ny))

    safe_areas = sum(row.count(0) for row in temp_matrix)
    return safe_areas

safeAreas, virusAreas = checkAreas(N, M, matrix)

for comb in combinations(safeAreas, 3):
    for cx, cy in comb:
        matrix[cx][cy] = 2
    safeAreas = checkSafeArea(N, M, matrix, virusAreas)
    answer = max(answer, safeAreas)
    for cx, cy in comb:
        matrix[cx][cy] = 0

print(answer)