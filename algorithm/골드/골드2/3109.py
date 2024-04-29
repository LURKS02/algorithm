from collections import deque

R, C = map(int, input().split())

matrix = []

dx = [1, 1, 1]
dy = [1, 0, -1]

for _ in range(R):
    matrix.append([c for c in input()])

def dfs(matrix, x, y):
    deq = deque()
    deq.append((x, y))

    while(deq):
        # print(deq)
        currentX, currentY = deq.pop()
        matrix[currentY][currentX] = 'x'

        if currentX == len(matrix[0]) - 1:
            return True

        for i in range(3):
            newX = currentX + dx[i]
            newY = currentY + dy[i]

            if 0 <= newX < len(matrix[0]) and 0 <= newY < len(matrix) and matrix[newY][newX] == '.':
                deq.append((newX, newY))

    return False

ans = 0
for k in range(R):
    if dfs(matrix, 0, k):
        ans += 1

# for i in range(R):
#     print(*matrix[i])
print(ans)
