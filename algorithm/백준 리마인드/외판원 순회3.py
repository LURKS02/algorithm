import math
import heapq

def distance(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

N = int(input())
cities = []

dist = [[0] * N for _ in range(N)]

for _ in range(N):
    x, y = map(int, input().split())
    cities.append((x, y))

for i in range(N):
    for j in range(N):
        dist[i][j] = distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])

cost = [[float('inf') for _ in range(1 << N)] for _ in range(N)]

cost[0][1] = 0
heap = []
heap.append((0, 1, 0))

answer = float('inf')

while heap:
    count, state, node = heapq.heappop(heap)

    if state == (1 << N) - 1:
        answer = min(answer, count + dist[node][0])
        continue

    for neighbor in range(N):
        if neighbor == node: continue

        if state & 1 << neighbor == 0:
            newState = state | 1 << neighbor
            newCost = count + dist[neighbor][node]
            if cost[neighbor][newState] > newCost:
                cost[neighbor][newState] = newCost
                heapq.heappush(heap, (newCost, newState, neighbor))

print(answer)