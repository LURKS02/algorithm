# N x M 크기의 격자 (100x100)
# K = 이동 가능한 상하좌우 칸 수 (5)
N, M, K = map(int, input().split())

board = [list(input()) for _ in range(N)]

# word = 영단어 (80)
word = input()

dpBoard = [[[-1 for _ in range(len(word) + 1)] for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(count, x, y):
    if dpBoard[x][y][count] != -1:
        return dpBoard[x][y][count]

    if count == len(word):
        return 1

    cnt = 0

    for k in range(1, K+1):
        for i in range(4):
            nx = x + dx[i]*k
            ny = y + dy[i]*k

            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == word[count]:
                cnt += dfs(count + 1, nx, ny)

    dpBoard[x][y][count] = cnt

    return cnt

answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == word[0]:
            answer += dfs(1, i, j)

print(answer)