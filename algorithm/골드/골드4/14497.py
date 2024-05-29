import heapq

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dijkstra(x1, y1):
    distance[x1-1][y1-1] = 0
    heap = []
    heapq.heappush(heap, (0, x1-1, y1-1))

    while heap:
        count, x, y = heapq.heappop(heap)
        if distance[x][y] < count:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == '0' and distance[nx][ny] > count:
                    heapq.heappush(heap, (count, nx, ny))
                    distance[nx][ny] = count

                elif board[nx][ny] == '1' and distance[nx][ny] > count + 1:
                    heapq.heappush(heap, (count+1, nx, ny))
                    distance[nx][ny] = count+1

                elif board[nx][ny] == '#':
                    return count + 1


N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
board = [[x for x in input()] for _ in range(N)]
INF = int(1e9)
distance = [[INF for _ in range(M)] for _ in range(N)]
print(dijkstra(x1, y1))