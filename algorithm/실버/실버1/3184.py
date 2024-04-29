import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
matrix = [input().rstrip() for _ in range(R)]

visited = [[False for _ in range(C)] for _ in range(R)]

def dfs_iterative(matrix, x, y):
    global wolf, lamb
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if not visited[x][y] and matrix[x][y] != '#':
            visited[x][y] = True
            if matrix[x][y] == 'v':
                wolf += 1
            if matrix[x][y] == 'o':
                lamb += 1

            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < R and 0 <= ny < C:
                    stack.append((nx, ny))

totalWolf = 0
totalLamb = 0

for i in range(R):
    for j in range(C):
        if not visited[i][j] and matrix[i][j] != '#':
            wolf, lamb = 0, 0
            dfs_iterative(matrix, i, j)
            if wolf < lamb:
                totalLamb += lamb
            else:
                totalWolf += wolf

print(totalLamb, totalWolf)
