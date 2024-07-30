N = int(input())
matrix = [list(input().split()) for _ in range(N)]

def calculate(A, B, op):
    if op == "+":
        return A+B
    elif op == "-":
        return A-B
    elif op == "*":
        return A * B

def solve(N, matrix):
    maxDP = [[-float('inf')] * N for _ in range(N)]
    minDP = [[float('inf')] * N for _ in range(N)]

    maxDP[0][0] = minDP[0][0] = int(matrix[0][0])

    for i in range(N):
        for j in range(N):
            if (i+j) % 2 == 1:
                maxDP[i][j] = max(maxDP[i-1][j], maxDP[i][j-1])
                minDP[i][j] = min(minDP[i-1][j], minDP[i][j-1])

            if i > 0:
                op = matrix[i-1][j]
                if (i-1 + j) % 2 == 1:
                    maxDP[i][j] = max(maxDP[i][j], calculate(maxDP[i-1][j], int(matrix[i][j]), op))
                    minDP[i][j] = min(minDP[i][j], calculate(minDP[i-1][j], int(matrix[i][j]), op))

            if j > 0:
                op = matrix[i][j-1]
                if (i + j-1) % 2 == 1:
                    maxDP[i][j] = max(maxDP[i][j], calculate(maxDP[i][j-1], int(matrix[i][j]), op))
                    minDP[i][j] = min(minDP[i][j], calculate(minDP[i][j-1], int(matrix[i][j]), op))

    return maxDP[N-1][N-1], minDP[N-1][N-1]

maxVal, minVal = solve(N, matrix)
print(maxVal, minVal)