from itertools import combinations
N, M = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# def bfs(x, y, city):
#     deq = deque()
#     deq.append((x, y))
#
#     visited = [[False for _ in range(N)] for _ in range(N)]
#
#     while(deq):
#         currentX, currentY = deq.popleft()
#         if city[currentY][currentX] == 2:
#             return abs(x - currentX) + abs(y - currentY)
#
#         for i in range(4):
#             newX, newY = currentX + dx[i], currentY + dy[i]
#             if 0 <= newX < N and 0 <= newY < N and not visited[newY][newX]:
#                 visited[newY][newX] = True
#                 deq.append((newX, newY))

city = [[int(i) for i in input().split()] for _ in range(N)]
homes = [(x, y) for x in range(N) for y in range(N) if city[y][x] == 1]
chickens = [(x, y) for x in range(N) for y in range(N) if city[y][x] == 2]


if len(chickens) > M:
    minChickenStreet = float('inf')

    for removableChicken in combinations(chickens, M):
        chickenStreet = 0

        for home in homes:
            chickenStreet += min([abs(home[0] - c[0]) + abs(home[1] - c[1]) for c in removableChicken])


        if minChickenStreet > chickenStreet:
            minChickenStreet = chickenStreet

    print(minChickenStreet)

else:
    minChickenStreet = float('inf')

    chickenStreet = 0

    for home in homes:
        chickenStreet += min([abs(home[0] - c[0]) + abs(home[1] - c[1]) for c in chickens])

    if minChickenStreet > chickenStreet:
        minChickenStreet = chickenStreet

    print(minChickenStreet)