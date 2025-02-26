from collections import deque

def solution(board):
    N = len(board)
    visited = [[[False] * 2 for _ in range(N)] for _ in range(N)]
    visited[0][0][0] = True

    deq = deque()
    deq.append([(0, 0), 0, 0])

    while deq:
        (x, y), position, count = deq.popleft()

        if position == 0:
            sx, sy = x, y + 1
            if (x == N-1 and y == N-1) or (sx == N-1 and sy == N-1):
                return count

            # 가로 - 오른쪽 이동
            ny = sy + 1
            if 0 <= ny < N and board[sx][ny] == 0 and not visited[sx][sy][0]:
                visited[sx][sy][0] = True
                deq.append([(sx, sy), 0, count+1])

            # 가로 - 왼쪽 이동
            ny = y - 1
            if 0 <= ny < N and board[x][ny] == 0 and not visited[x][ny][0]:
                visited[x][ny][0] = True
                deq.append([(x, ny), 0, count+1])

            # 가로 - 위 이동
            nx = x - 1
            if 0 <= nx < N and board[nx][y] == 0 and board[nx][sy] == 0 and not visited[nx][y][0]:
                visited[nx][y][0] = True
                deq.append([(nx, y), 0, count+1])

            # 가로 - 아래 이동
            nx = x + 1
            if 0 <= nx < N and board[nx][y] == 0 and board[nx][sy] == 0 and not visited[nx][y][0]:
                visited[nx][y][0] = True
                deq.append([(nx, y), 0, count+1])

            # 가로 - 아래로 회전
            nx = x + 1
            if 0 <= nx < N and board[nx][y] == 0 and board[nx][sy] == 0:
                if not visited[x][y][1]:
                    visited[x][y][1] = True
                    deq.append([(x, y), 1, count+1])
                if not visited[x][sy][1]:
                    visited[x][sy][1] = True
                    deq.append([(x, sy), 1, count+1])

            # 가로 - 위로 회전
            nx = x - 1
            if 0 <= nx < N and board[nx][y] == 0 and board[nx][sy] == 0:
                if not visited[nx][y][1]:
                    visited[nx][y][1] = True
                    deq.append([(nx, y), 1, count+1])
                if not visited[nx][sy][1]:
                    visited[nx][sy][1] = True
                    deq.append([(nx, sy), 1, count+1])

        else:
            sx, sy = x + 1, y
            if (x == N - 1 and y == N - 1) or (sx == N - 1 and sy == N - 1):
                return count

            # 세로 - 위 이동
            nx = x - 1
            if 0 <= nx < N and board[nx][y] == 0 and not visited[nx][y][1]:
                visited[nx][y][1] = True
                deq.append([(nx, y), 1, count + 1])

            # 세로 - 아래 이동
            nx = sx + 1
            if 0 <= nx < N and board[nx][y] == 0 and not visited[sx][y][1]:
                visited[sx][y][1] = True
                deq.append([(sx, y), 1, count+1])

            # 세로 - 오른쪽 이동
            ny = y + 1
            if 0 <= ny < N and board[x][ny] == 0 and board[sx][ny] == 0 and not visited[x][ny][1]:
                visited[x][ny][1] = True
                deq.append([(x, ny), 1, count+1])

            # 세로 - 왼쪽 이동
            ny = y - 1
            if 0 <= ny < N and board[x][ny] == 0 and board[sx][ny] == 0 and not visited[x][ny][1]:
                visited[x][ny][1] = True
                deq.append([(x, ny), 1, count+1])

            # 세로 - 오른쪽 회전
            ny = y + 1
            if 0 <= ny < N and board[x][ny] == 0 and board[sx][ny] == 0:
                if not visited[x][y][0]:
                    visited[x][y][0] = True
                    deq.append([(x, y), 0, count+1])
                if not visited[sx][y][0]:
                    visited[sx][y][0] = True
                    deq.append([(sx, y), 0, count+1])

            # 세로 - 왼쪽 회전
            ny = y - 1
            if 0 <= ny < N and board[x][ny] == 0 and board[sx][ny] == 0:
                if not visited[x][ny][0]:
                    visited[x][ny][0] = True
                    deq.append([(x, ny), 0, count+1])
                if not visited[sx][ny][0]:
                    visited[sx][ny][0] = True
                    deq.append([(sx, ny), 0, count+1])

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))