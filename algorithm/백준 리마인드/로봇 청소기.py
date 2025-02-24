import heapq

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    matrix = [list(input()) for _ in range(h)]

    startX, startY = -1, -1
    indexMatrix = [[-1] * w for _ in range(h)]
    startIndex = 0

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 'o':
                startX, startY = i, j

            if matrix[i][j] == '*':
                indexMatrix[i][j] = startIndex
                startIndex += 1

    heap = []
    heapq.heappush(heap, (0, 0, startX, startY))

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    cost = [[[float('inf')] * 20 for _ in range(20)] for _ in range(1024)]
    cost[0][0][0] = 0

    printed = False

    while heap:
        count, bit, x, y = heapq.heappop(heap)

        bit = -bit

        if bit == (1 << startIndex) - 1:
            print(count)
            printed = True
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] != 'x':
                if indexMatrix[nx][ny] != -1:
                    newbit = bit | (1 << indexMatrix[nx][ny])
                    if cost[newbit][nx][ny] > count+1:
                        cost[newbit][nx][ny] = count+1
                        heapq.heappush(heap, (count+1, -newbit, nx, ny))
                else:
                    if cost[bit][nx][ny] > count+1:
                        cost[bit][nx][ny] = count + 1
                        heapq.heappush(heap, (count+1, -bit, nx, ny))

    if not printed:
        print(-1)
