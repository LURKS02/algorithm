# 입력 받기
N = int(input())
board = [list(input().strip()) for _ in range(N)]

# 방향벡터 (상하좌우, 대각선)
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# 지뢰를 설치할 수 있는지 확인
def can_place_mine(i, j):
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj] != '#' and board[ni][nj] != '*':
                mine_count = sum(board[ni + di][nj + dj] == '*' for di, dj in directions if 0 <= ni + di < N and 0 <= nj + dj < N)
                if mine_count >= int(board[ni][nj]):
                    return False
    return True

# 최대한 많은 지뢰를 설치
mine_count = 0
for i in range(1, N-1):
    for j in range(1, N-1):
        if board[i][j] == '#' and can_place_mine(i, j):
            board[i][j] = '*'
            mine_count += 1

# 출력
print(mine_count)