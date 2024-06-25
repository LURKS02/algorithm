from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magics = [tuple(map(int, input().split())) for _ in range(M)]

sharkR = (N+1)//2-1
sharkC = (N+1)//2-1

def sortBoard(board):
    N = len(board)
    centerR = (N+1)//2-1
    centerC = (N+1)//2-1

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    deq = deque()
    length = 1
    direction = 0

    nx, ny = centerR, centerC
    while True:
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            break

        for _ in range(length):
            nx += dx[direction]
            ny += dy[direction]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] != 0:
                    deq.append(board[nx][ny])

            else:
                break

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            break

        direction = (direction+1) % 4

        for _ in range(length):
            nx += dx[direction]
            ny += dy[direction]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] != 0:
                    deq.append(board[nx][ny])
            else:
                break

        length += 1
        direction = (direction + 1) % 4

    return deq

def breakBalls(balls):
    canceledBalls = [0]*4
    tempVal = -1
    tempArr = deque()
    resultArr = deque()

    for ball in balls:
        if len(tempArr) == 0:
            tempVal = ball
            tempArr.append(ball)
        else:
            if tempVal == ball:
                tempArr.append(ball)

            else:
                if len(tempArr) >= 4:
                    canceledBalls[tempVal] += len(tempArr)
                    tempArr = deque([ball])
                    tempVal = ball
                else:
                    for i in range(len(tempArr)):
                        resultArr.append(tempVal)
                    tempArr = deque([ball])
                    tempVal = ball

    if len(tempArr) >= 4:
        canceledBalls[tempVal] += len(tempArr)
    else:
        for i in range(len(tempArr)):
            resultArr.append(tempVal)

    return resultArr, canceledBalls

def increaseBall(balls):
    tempVal = -1
    tempArr = deque()
    resultArr = deque()

    for ball in balls:
        if len(tempArr) == 0:
            tempVal = ball
            tempArr.append(ball)
        else:
            if tempVal == ball:
                tempArr.append(ball)
            else:
                resultArr.append(len(tempArr))
                resultArr.append(tempVal)
                tempVal = ball
                tempArr = deque([ball])

    if len(tempArr) > 0:
        resultArr.append(len(tempArr))
        resultArr.append(tempVal)

    return resultArr

def makeMatrix(deq):
    tempMatrix = [[0] * N for _ in range(N)]
    nx = (N + 1) // 2 - 1
    ny = (N + 1) // 2 - 1

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    length = 1
    direction = 0

    while deq:
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            break

        for _ in range(length):
            nx += dx[direction]
            ny += dy[direction]
            if 0 <= nx < N and 0 <= ny < N and deq:
                tempMatrix[nx][ny] = deq.popleft()
            else:
                break

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            break
        direction = (direction + 1) % 4

        for _ in range(length):
            nx += dx[direction]
            ny += dy[direction]
            if 0 <= nx < N and 0 <= ny < N and deq:
                tempMatrix[nx][ny] = deq.popleft()
            else:
                break

        length += 1
        direction = (direction + 1) % 4

    return tempMatrix

balls = [0] * 4

for magic in magics:
    d, s = magic

    for i in range(1, s+1):
        if d == 1:
            # balls[board[sharkR-i][sharkC]] += 1
            board[sharkR-i][sharkC] = 0
        elif d == 2:
            # balls[board[sharkR+i][sharkC]] += 1
            board[sharkR+i][sharkC] = 0
        elif d == 3:
            # balls[board[sharkR][sharkC-i]] += 1
            board[sharkR][sharkC-i] = 0
        elif d == 4:
            # balls[board[sharkR][sharkC+i]] += 1
            board[sharkR][sharkC+i] = 0

    ballDeq = sortBoard(board)

    while True:
        ballDeq, canceledBalls = breakBalls(ballDeq)
        if sum(canceledBalls) == 0:
            break
        for i in range(4):
            balls[i] += canceledBalls[i]

    ballDeq = increaseBall(ballDeq)

    # print(ballDeq)
    board = makeMatrix(ballDeq)

print(balls[1] + 2*balls[2] + 3*balls[3])