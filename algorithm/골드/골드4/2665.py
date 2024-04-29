import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N = int(input())
room = []

for _ in range(N):
    room.append(list(map(int, input().rstrip())))
visited = [[False] * N for _ in range(N)]

def dijkstra():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    heap = []
    heappush(heap, (0, 0, 0))
    visited[0][0] = True

    while heap:
        count, x, y = heappop(heap)
        if x == N-1 and y == N-1:
            print(count)
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                if room[nx][ny] == 0:
                    heappush(heap, (count + 1, nx, ny))
                else:
                    heappush(heap, (count, nx, ny))

dijkstra()