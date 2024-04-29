N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
maxValue = 1

def getMax(matrix):
    maxV = 1
    for i in range(N):
        for j in range(N):
            if maxV < matrix[i][j]:
                maxV = matrix[i][j]
    return maxV

def moveDown(board):
    resultArray = [[0] * N for _ in range(N)]

    for j in range(N):
        tempList = [0] * N
        returnList = [0] * N
        visited = [False] * N
        tempStart = N-1
        for i in range(N-1, -1, -1):
            if board[i][j] != 0:
                tempList[tempStart] = board[i][j]
                tempStart -= 1
        # print(tempList)

        returnStart = N-1
        for i in range(N-1, -1, -1):
            if tempList[i] == 0:
                break
            else:
                if i == 0:
                    if not visited[i]:
                        visited[i] = True
                        returnList[returnStart] = tempList[i]
                        returnStart -= 1

                elif tempList[i] == tempList[i - 1] and not visited[i] and not visited[i-1]:
                    visited[i] = True
                    visited[i-1] = True
                    newValue = tempList[i] + tempList[i - 1]
                    returnList[returnStart] = newValue
                    returnStart -= 1
                elif tempList[i] != tempList[i - 1] and not visited[i]:
                    visited[i] = True
                    returnList[returnStart] = tempList[i]
                    returnStart -= 1

        for i in range(N):
            resultArray[i][j] = returnList[i]
    return resultArray

def moveUp(board):
    resultArray = [[0] * N for _ in range(N)]

    for j in range(N):
        tempList = [0] * N
        returnList = [0] * N
        visited = [False] * N
        tempStart = 0
        for i in range(N):
            if board[i][j] != 0:
                tempList[tempStart] = board[i][j]
                tempStart += 1
        # print(tempList)

        returnStart = 0
        for i in range(N):
            if tempList[i] == 0:
                break
            else:
                if i == N-1:
                    if not visited[i]:
                        visited[i] = True
                        returnList[returnStart] = tempList[i]
                        returnStart += 1

                elif tempList[i] == tempList[i + 1] and not visited[i] and not visited[i+1]:
                    visited[i] = True
                    visited[i+1] = True
                    newValue = tempList[i] + tempList[i + 1]
                    returnList[returnStart] = newValue
                    returnStart += 1
                elif tempList[i] != tempList[i + 1] and not visited[i]:
                    visited[i] = True
                    returnList[returnStart] = tempList[i]
                    returnStart += 1

        for i in range(N):
            resultArray[i][j] = returnList[i]
    return resultArray

def moveLeft(board):
    resultArray = []

    for i in range(N):
        tempList = [0] * N
        returnList = [0] * N
        visited = [False] * N
        tempStart = 0
        for j in range(N):
            if board[i][j] != 0:
                tempList[tempStart] = board[i][j]
                tempStart += 1
        #print(tempList)

        returnStart = 0
        for j in range(N):
            if tempList[j] == 0:
                break
            else:
                if j == N-1:
                    if not visited[j]:
                        visited[j] = True
                        returnList[returnStart] = tempList[j]
                        returnStart += 1

                elif tempList[j] == tempList[j + 1] and not visited[j] and not visited[j+1]:
                    visited[j] = True
                    visited[j+1] = True
                    newValue = tempList[j] + tempList[j + 1]
                    returnList[returnStart] = newValue
                    returnStart += 1
                elif tempList[j] != tempList[j + 1] and not visited[j]:
                    visited[j] = True
                    returnList[returnStart] = tempList[j]
                    returnStart += 1

        resultArray.append(returnList)
    return resultArray

def moveRight(board):
    resultArray = []

    for i in range(N):
        tempList = [0] * N
        returnList = [0] * N
        visited = [False] * N
        tempStart = N-1
        for j in range(N-1, -1, -1):
            if board[i][j] != 0:
                tempList[tempStart] = board[i][j]
                tempStart -= 1
        # print(tempList)

        returnStart = N-1
        for j in range(N-1, -1, -1):
            if tempList[j] == 0:
                break
            else:
                if j == 0:
                    if not visited[j]:
                        visited[j] = True
                        returnList[returnStart] = tempList[j]
                        returnStart -= 1

                elif tempList[j] == tempList[j - 1] and not visited[j] and not visited[j - 1]:
                    visited[j] = True
                    visited[j-1] = True
                    newValue = tempList[j] + tempList[j-1]
                    returnList[returnStart] = newValue
                    returnStart -= 1
                elif tempList[j] != tempList[j - 1] and not visited[j]:
                    visited[j] = True
                    returnList[returnStart] = tempList[j]
                    returnStart -= 1

        resultArray.append(returnList)
    return resultArray

# result = moveDown()
# for i in range(N):
#     print(*result[i])

def dfs(board, depth):
    if depth == 5:
        return max(map(max, board))

    max_block = 0
    for move in (moveRight, moveLeft, moveDown, moveUp):
        new_board = move(board)
        max_block = max(max_block, dfs(new_board, depth + 1))

    return max_block

result = dfs(board, 0)
print(result)
