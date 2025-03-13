import heapq
from collections import defaultdict
M, N = map(int, input().split())

matrix = []

startX = -1
startY = -1
endX = -1
endY = -1

items = defaultdict()

# 아이템이 5개까지 있는데, 이걸 set형태로 가지고 있어도 될 것 같고,
# 어차피 방문 처리를 안하면 시간 제한에 걸릴 수도 있을 것 같은데 차라리 비트마스킹을 써야겠다는 생각

itemNumber = 1
for i in range(N):
    l = list(input())
    for j in range(M):
        if l[j] == "S":
            startX, startY = i, j
        elif l[j] == "E":
            endX, endY = i, j
        elif l[j] == "X":
            l[j] = str(itemNumber)
            itemNumber += 1

    matrix.append(l)

heap = []
heap.append((0, 0, startX, startY))
target = (1 << (itemNumber-1)) - 1
cost = [[[float('inf')] * (target+1) for _ in range(M)] for _ in range(N)]
cost[startX][startY][0] = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while heap:
    count, visited, x, y = heapq.heappop(heap)

    if x == endX and y == endY and visited == target:
        print(count)
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] != "#":
            newCount = count + 1
            newVisited = visited
            if matrix[nx][ny] in ["1", "2", "3", "4", "5"]:
                newVisited = visited | (1 << (int(matrix[nx][ny]) - 1))
            if cost[nx][ny][newVisited] > newCount:
                cost[nx][ny][newVisited] = newCount
                heapq.heappush(heap, (newCount, newVisited, nx, ny))


