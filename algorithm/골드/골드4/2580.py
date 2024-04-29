board = [list(map(int, input().split())) for _ in range(9)]

def isValid(num, row, col):
    if num in board[row]:
        return False
    if num in (board[i][col] for i in range(9)):
        return False

    start_row, start_col =  3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if isValid(num, i, j):
                        board[i][j] = num
                        if solve():
                            return True
                        board[i][j] = 0
                return False

    return True

solve()
for i in range(9):
    print(*board[i])
