N = int(input())
square = [[0 for _ in range(100)] for _ in range(100)]

count = 0

for _ in range(N):
    X, Y = map(int, input().split())
    for i in range(X, X + 10):
        for j in range(Y, Y + 10):
            if square[i][j] == 0:
                square[i][j] = 1
                count += 1

print(count)