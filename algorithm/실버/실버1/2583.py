import sys
sys.setrecursionlimit(10**9)

M, N, K = map(int, input().split())

matrix = [[True for _ in range(M)] for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            #print(x, y)
            matrix[x][y] = False

def dfs(x, y, matrix):
    if x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[0]) and matrix[x][y] == True:
        matrix[x][y] = False
        global globalarea
        globalarea += 1

        dfs(x-1, y, matrix)
        dfs(x+1, y, matrix)
        dfs(x, y-1, matrix)
        dfs(x, y+1, matrix)

        return True

    else:
        return False

cnt = 0
area = []

for x in range(N):
    for y in range(M):
        # print(x, y)
        globalarea = 0
        if dfs(x, y, matrix) == True:
            cnt += 1
        if globalarea != 0:
            area.append(globalarea)

print(cnt)
print(*sorted(area))