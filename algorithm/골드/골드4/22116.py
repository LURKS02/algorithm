import sys
from collections import deque
input = sys.stdin.readline

# N = 격자의 크기
N = int(input().rstrip())

# matrix = 격자
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

def bfs(dist):
    deq = deque()
    visited = [[False] * N for _ in range(N)]
    deq.append((0, 0))
    visited[0][0] = True

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                value = abs(matrix[x][y] - matrix[nx][ny])
                if value <= dist:
                    if nx == N-1 and ny == N-1: return True
                    deq.append((nx, ny))
                    visited[nx][ny] = True

    return False

answer = 0
left = 0
right = 1000000000

while left <= right:
    mid = (left + right) // 2

    if bfs(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
