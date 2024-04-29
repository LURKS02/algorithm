import sys
sys.setrecursionlimit(10**9)

N, M, K = map(int, input().split())

matrix = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = 1

def dfs(x, y):
    global count
    if x >= 0 and y >= 0 and x < N and y < M and matrix[x][y] == 1:
        matrix[x][y] = 0
        count += 1

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

count = 0
maxval = 0
for i in range(N):
    for j in range(M):
        dfs(i, j)
        if maxval < count:
            maxval = count
        count = 0


print(maxval)