import copy

matrix = [[False for _ in range(10)] for _ in range(10)]

ans = 101
dx = [0, -1, 0, 1, 0]
dy = [1, 0, 0, 0, -1]

def push(board, x, y):
    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= 9 and 0 <= ny <= 9:
            board[nx][ny] = not board[nx][ny]

for i in range(10):
    line = list(input())
    for j in range(10):
        if line[j] == 'O':
            matrix[i][j] = True

for i in range(1 << 10):
    temp = copy.deepcopy(matrix)
    cnt = 0

    for j in range(10):
        if i & (1 << j):
            cnt += 1
            push(temp, 0, j)

    for j in range(1, 10):
        for k in range(10):
            if temp[j-1][k]:
                push(temp, j, k)
                cnt += 1

    if not any(temp[9]):
        ans = min(ans, cnt)

print(ans if ans != 101 else -1)