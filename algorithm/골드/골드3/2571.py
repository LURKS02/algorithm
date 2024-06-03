board = [[0 for _ in range(101)] for _ in range(101)]

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())

    for i in range(a, a + 10):
        for j in range(b, b + 10):
            board[i][j] = 1

answer = 0

for i in range(100):
    for j in range(101):
        if board[i][j] != 0 and board[i+1][j] != 0:
            board[i+1][j] = board[i][j] + 1



for i in range(101):
    for j in range(101):
        h = 100
        for k in range(j, 100):
            h = min(h, board[i][k])
            if h == 0:
                break
            answer = max(answer, h * (k - j + 1))

print(answer)
