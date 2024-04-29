from collections import deque

N, L, R = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(startX, startY, visited):
    deq = deque([(startX, startY)])
    visited[startY][startX] = True
    union = [(startX, startY)]

    while(deq):
        currentX, currentY = deq.popleft()

        for i in range(4):
            newX = currentX + dx[i]
            newY = currentY + dy[i]

            if 0 <= newX < N and 0 <= newY < N and not visited[newY][newX] and L <= abs(matrix[currentY][currentX] - matrix[newY][newX]) <= R:
                visited[newY][newX] = True
                union.append((newX, newY))
                deq.append((newX, newY))
    return union

day = 0

while True:
    unions = []
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result = bfs(j, i, visited)
                if len(result) > 1:
                    unions.append(result)

    if len(unions) == 0:
        break

    else:
        # print(unions)

        for union in unions:
            s = sum([matrix[y][x] for x, y in union])
            l = len(union)

            people = s // l
            # print(s, l, people)

            for x, y in union:
                matrix[y][x] = people

        # for i in range(N):
        #     print(*matrix[i])

    day += 1

print(day)
