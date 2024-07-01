import sys
input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
matrix = [[float('inf')] * V for _ in range(V)]

for _ in range(E):
    x, y, c = map(int, input().split())
    matrix[x-1][y-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

answer = float('inf')
for i in range(V):
    answer = min(answer, matrix[i][i])

if answer == float('inf'):
    print(-1)
else:
    print(answer)