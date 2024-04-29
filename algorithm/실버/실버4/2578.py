
board = []

for _ in range(5):
    l = list(map(int, input().split()))
    board.append(l)

def findNum(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0
                return

def checkBingo(board):
    count = 0
    for i in range(5):
        if all(board[i][j] == 0 for j in range(5)):
            count += 1
    for j in range(5):
        if all(board[i][j] == 0 for i in range(5)):
            count += 1
    if all(board[i][i] == 0 for i in range(5)):
        count += 1
    if all(board[j][4 - j] == 0 for j in range(5)):
        count += 1
    return count


count = 0
for _ in range(5):
    breakPoint = False
    l = list(map(int, input().split()))
    for num in l:
        findNum(board, num)
        count += 1
        if checkBingo(board) >= 3:
            breakPoint = True
            break
    if breakPoint:
        break
print(count)

