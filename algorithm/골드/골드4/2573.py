from collections import deque

N, M = map(int, input().split()) # N: 행의 개수, M: 열의 개수
iceberg = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt():
    next_iceberg = [[0]*M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if iceberg[x][y] > 0:
                count = 0
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M and iceberg[nx][ny] == 0:
                        count += 1
                next_iceberg[x][y] = max(iceberg[x][y] - count, 0)
    return next_iceberg

def count_chunks():
    visited = [[False]*M for _ in range(N)]
    chunks = 0
    for x in range(N):
        for y in range(M):
            if iceberg[x][y] > 0 and not visited[x][y]:
                chunks += 1
                queue = deque([(x, y)])
                visited[x][y] = True
                while queue:
                    cx, cy = queue.popleft()
                    for d in range(4):
                        nx, ny = cx + dx[d], cy + dy[d]
                        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and iceberg[nx][ny] > 0:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
    return chunks

year = 0
while True:
    year += 1
    iceberg = melt()
    chunks = count_chunks()
    if chunks > 1:
        print(year)
        break
    elif chunks == 0:
        print(0)
        break