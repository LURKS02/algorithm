import math
from collections import deque
from collections import defaultdict

n, k = map(int, input().split())
spots = [(0, 0), (10000, 10000)]

graph = defaultdict(list)

for _ in range(n):
    x, y = map(int, input().split())
    spots.append((x, y))

for i in range(len(spots)):
    for j in range(i+1, len(spots)):
        length = math.ceil(math.sqrt(pow(spots[i][0] - spots[j][0], 2) + pow(spots[i][1] - spots[j][1], 2)) / 10)
        graph[spots[i]].append((spots[j], length))
        graph[spots[j]].append((spots[i], length))

# print(graph[(10, 1000)])

start = 0
end = math.ceil(math.ceil(math.sqrt(pow(10000, 2) + pow(10000, 2))) / 10)
ans = 0

while start <= end:
    mid = (start + end) // 2

    def BFS(mid):
        cost = {}
        for spot in spots:
            cost[spot] = float('inf')
        deq = deque([((0, 0), 0)])
        cost[(0, 0)] = 0

        while deq:
            point, val = deq.popleft()

            if val == k+1:
                continue

            for neighbor, length in graph[point]:
                if length <= mid and val + 1 < cost[neighbor]:
                    deq.append((neighbor, val + 1))
                    cost[neighbor] = val + 1

        return cost[(10000, 10000)]

    v = BFS(mid)
    if v != float('inf'):
        ans = mid
        end = mid - 1

    else:
        start = mid + 1

print(ans)