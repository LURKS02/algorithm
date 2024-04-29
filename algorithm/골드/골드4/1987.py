import sys
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())

matrix = []

for _ in range(R):
    matrix.append([c for c in input().rstrip()])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

s = set()
s.add(matrix[0][0])
maxCount = -1
def dfs(matrix, x, y):
    global maxCount

    if maxCount < len(s):
        maxCount = len(s)

    for i in range(4):
        newX, newY = x + dx[i], y + dy[i]
        if 0 <= newX < C and 0 <= newY < R and matrix[newY][newX] not in s:
            s.add(matrix[newY][newX])
            dfs(matrix, newX, newY)
            s.remove(matrix[newY][newX])

dfs(matrix, 0, 0)
print(maxCount)