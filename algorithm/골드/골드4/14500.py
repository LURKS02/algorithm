N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

ans = -float('inf')

def check1_1():
    maxValue = -float('inf')
    for i in range(N):
        for j in range(0, M-3):
            value = board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3]
            maxValue = max(maxValue, value)
    return maxValue

def check1_2():
    maxValue = -float('inf')
    for i in range(0, N-3):
        for j in range(M):
            value = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]
            maxValue = max(maxValue, value)
    return maxValue

def check2():
    maxValue = -float('inf')
    for i in range(0, N-1):
        for j in range(0, M-1):
            value = board[i][j] + board[i+1][j] + board[i][j+1] + board[i+1][j+1]
            maxValue = max(maxValue, value)
    return maxValue

def check3_1():
    maxValue = -float('inf')
    for i in range(0, N-2):
        for j in range(0, M-1):
            value = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j+1]
            maxValue = max(maxValue, value)
    return maxValue

def check3_2():
    maxValue = -float('inf')
    for i in range(1, N):
        for j in range(0, M-2):
            value = board[i][j] + board[i][j+1] + board[i][j+2] + board[i-1][j+2]
            maxValue = max(maxValue, value)
    return maxValue

def check3_3():
    maxValue = -float('inf')
    for i in range(0, N-2):
        for j in range(0, M-1):
            value = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1]
            maxValue = max(maxValue, value)
    return maxValue

def check3_4():
    maxValue = -float('inf')
    for i in range(0, N-1):
        for j in range(0, M-2):
            value = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j]
            maxValue = max(maxValue, value)
    return maxValue

def check4_1():
    maxValue = -float('inf')
    for i in range(0, N-2):
        for j in range(0, M-1):
            value = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
            maxValue = max(maxValue, value)
    return maxValue

def check4_2():
    maxValue = -float('inf')
    for i in range(1, N):
        for j in range(0, M-2):
            value = board[i][j] + board[i][j+1] + board[i-1][j+1] + board[i-1][j+2]
            maxValue = max(maxValue, value)
    return maxValue

def check5_1():
    maxValue = -float('inf')
    for i in range(0, N-1):
        for j in range(0, M-2):
            value = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1]
            maxValue = max(maxValue, value)
    return maxValue

def check5_2():
    maxValue = -float('inf')
    for i in range(0, N-2):
        for j in range(0, M-1):
            value = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+1][j+1]
            maxValue = max(maxValue, value)
    return maxValue

def check5_3():
    maxValue = -float('inf')
    for i in range(1, N):
        for j in range(0, M-2):
            value = board[i][j] + board[i][j+1] + board[i][j+2] + board[i-1][j+1]
            maxValue = max(maxValue, value)
    return maxValue

def check5_4():
    maxValue = -float('inf')
    for i in range(1, N-1):
        for j in range(0, M-1):
            value = board[i][j] + board[i-1][j+1] + board[i][j+1] + board[i+1][j+1]
            maxValue = max(maxValue, value)
    return maxValue

def check6_1():
    maxValue = -float('inf')
    for i in range(2, N):
        for j in range(0, M-1):
            value = board[i][j] + board[i][j+1] + board[i-1][j+1] + board[i-2][j+1]
            maxValue = max(maxValue, value)
    return maxValue

def check6_2():
    maxValue = -float('inf')
    for i in range(0, N-1):
        for j in range(0, M-2):
            value = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+2]
            maxValue = max(maxValue, value)
    return maxValue

def check6_3():
    maxValue = -float('inf')
    for i in range(0, N-2):
        for j in range(0, M-1):
            value = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+2][j]
            maxValue = max(maxValue, value)
    return maxValue

def check6_4():
    maxValue = -float('inf')
    for i in range(0, N-1):
        for j in range(0, M-2):
            value = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
            maxValue = max(maxValue, value)
    return maxValue

def check7_1():
    maxValue = -float('inf')
    for i in range(1, N-1):
        for j in range(0, M-1):
            value = board[i][j] + board[i+1][j] + board[i][j+1] + board[i-1][j+1]
            maxValue = max(maxValue, value)
    return maxValue

def check7_2():
    maxValue = -float('inf')
    for i in range(0, N-1):
        for j in range(0, M-2):
            value = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2]
            maxValue = max(maxValue, value)
    return maxValue

ans = max(check1_1(), check1_2(), check2(), check3_1(), check3_2(), check3_3(), check3_4(), check4_1(), check4_2(), check5_1(), check5_2(), check5_3(), check5_4(), check6_1(), check6_2(), check6_3(), check6_4(), check7_1(), check7_2())
print(ans)