import sys
import heapq

def dijkstra(N, matrix):
    costs = [[float('inf')] * N for _ in range(N)]
    costs[0][0] = matrix[0][0]
    heap = [(matrix[0][0], 0, 0)] # 비용, x, y

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap:
        currentCost, x, y = heapq.heappop(heap)

        if x == N-1 and y == N-1:
            return currentCost

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                newCost = currentCost + matrix[nx][ny]
                if newCost < costs[nx][ny]:
                    costs[nx][ny] = newCost
                    heapq.heappush(heap, (newCost, nx, ny))


num = 1
while True:
    N = int(input())
    if N == 0:
        break

    matrix = [list(map(int, input().split())) for _ in range(N)]

    print("Problem " + str(num) + ": " + str(dijkstra(N, matrix)))

    num += 1