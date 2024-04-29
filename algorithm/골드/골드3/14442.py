from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]

def bfs():
    deq = deque()
    deq.append([0, 0, K])
    visited[0][0][K] = 1

    while deq:
        x, y, z = deq.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][z]

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and z > 0 and not visited[nx][ny][z-1]:
                    visited[nx][ny][z-1] = visited[x][y][z] + 1
                    deq.append([nx, ny, z-1])
                elif arr[nx][ny] == 0 and not visited[nx][ny][z]:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    deq.append([nx, ny, z])

    return -1

print(bfs())

