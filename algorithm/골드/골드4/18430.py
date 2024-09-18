N, M = map(int, input().split())
K = []

for _ in range(N):
    l = list(map(int, input().split()))
    K.append([[num, False] for num in l])

maxSum = 0

def backtracking(x, y, count):
    # print(x, y, count)
    global maxSum

    if x == N-1 and y == M-1:
        maxSum = max(maxSum, count)
        return

    if K[x][y][1]:
        if y+1 < M:
            backtracking(x, y+1, count)
        else:
            backtracking(x+1, 0, count)

    else:
        if x+1 < N and y+1 < M and not K[x][y][1] and not K[x+1][y+1][1] and not K[x][y+1][1]:
            K[x][y][1] = True
            K[x+1][y+1][1] = True
            K[x][y+1][1] = True
            backtracking(x, y+1, count + K[x][y][0] + 2*K[x][y+1][0] + K[x+1][y+1][0])
            K[x][y][1] = False
            K[x + 1][y + 1][1] = False
            K[x][y + 1][1] = False

        if x+1 < N and y-1 >= 0 and not K[x][y][1] and not K[x+1][y-1][1] and not K[x+1][y][1]:
            K[x][y][1] = True
            K[x+1][y-1][1] = True
            K[x+1][y][1] = True
            if y+1 < M:
                backtracking(x, y+1, count + K[x][y][0] + 2*K[x+1][y][0] + K[x+1][y-1][0])
            else:
                backtracking(x+1, 0, count + K[x][y][0] + 2*K[x+1][y][0] + K[x+1][y-1][0])
            K[x][y][1] = False
            K[x + 1][y - 1][1] = False
            K[x + 1][y][1] = False

        if x+1 < N and y+1 < M and not K[x][y][1] and not K[x+1][y][1] and not K[x+1][y+1][1]:
            K[x][y][1] = True
            K[x+1][y][1] = True
            K[x+1][y+1][1] = True
            backtracking(x, y+1, count + K[x][y][0] + 2*K[x+1][y][0] + K[x+1][y+1][0])
            K[x][y][1] = False
            K[x + 1][y][1] = False
            K[x + 1][y + 1][1] = False

        if x+1 < N and y+1 < M and not K[x][y][1] and not K[x][y+1][1] and not K[x+1][y][1]:
            K[x][y][1] = True
            K[x][y+1][1] = True
            K[x+1][y][1] = True
            backtracking(x, y+1, count + 2*K[x][y][0] + K[x][y+1][0] + K[x+1][y][0])
            K[x][y][1] = False
            K[x][y + 1][1] = False
            K[x + 1][y][1] = False

        if y+1 < M:
            backtracking(x, y+1, count)
        else:
            backtracking(x+1, 0, count)



backtracking(0, 0, 0)
print(maxSum)