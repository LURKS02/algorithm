from collections import deque

# N = 격자의 크기 (6, 2^N)
# Q = 파이어 스톰의 시전 횟수 (1000)
N, Q = map(int, input().split())
N = pow(2, N)

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

magics = list(map(int, input().split()))

def changeMagic(degree):
    if degree == 0:
        return

    changeN = pow(2, degree)

    for i in range(0, N, changeN):
        for j in range(0, N, changeN):
            startI = i
            startJ = j

            tempMatrix = [[-1] * changeN for _ in range(changeN)]
            temp = changeN-1

            for m in range(changeN):
                l = []
                for n in range(changeN):
                    l.append(board[startI + m][startJ + n])
                for k in range(len(l)):
                    tempMatrix[k][temp] = l[k]
                temp -= 1
            for m in range(changeN):
                for n in range(changeN):
                    board[startI + m][startJ + n] = tempMatrix[m][n]

    # for m in range(N):
    #     print(*board[m])
    # print()

def removeIce():
    removeList = []

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(N):
        for j in range(N):
            ices = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]

                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 0:
                    ices += 1

            if ices < 3:
                removeList.append((i, j))

    for rx, ry in removeList:
        if board[rx][ry] > 0:
            board[rx][ry] -= 1

    # for m in range(N):
    #     print(*board[m])
    # print()

def totalIces():
    total = 0
    for i in range(N):
        for j in range(N):
            total += board[i][j]

    return total

def findMaxIce(x, y, visited):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    deq = deque()
    deq.append((x, y))
    visited[x][y] = True

    count = 0
    while deq:
        curX, curY = deq.popleft()
        count += 1

        for i in range(4):
            nx, ny = curX + dx[i], curY + dy[i]

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                deq.append((nx, ny))

    return count

for magic in magics:
    changeMagic(magic)
    removeIce()


visited = [[False] * N for _ in range(N)]
maxIce = 0
for i in range(N):
    for j in range(N):
        if board[i][j] != 0 and not visited[i][j]:
            maxIce = max(maxIce, findMaxIce(i, j, visited))

print(totalIces())
print(maxIce)
