def solution(key, lock):
    answer = False

    M = len(key)
    N = len(lock)

    newMatrix = [[0] * (N + 2*M) for _ in range(N + 2*M)]

    for i in range(M, M + N):
        for j in range(M, M + N):
            newMatrix[i][j] = lock[i-M][j-M]

    # for i in range(len(newMatrix)):
    #     print(*newMatrix[i])

    def rotateMatrix(matrix):
        row = len(matrix)
        col = len(matrix[0])
        newMatrix = [[0] * row for _ in range(col)]

        for i in range(row):
            rowList = matrix[i]
            for j in range(col):
                newMatrix[j][row - i - 1] = matrix[i][j]

        return newMatrix

    for _ in range(4):
        for i in range(0, len(newMatrix) - M + 1):
            for j in range(0, len(newMatrix) - M + 1):
                canMake = True
                for m in range(M):
                    for n in range(M):
                        newMatrix[i+m][j+n] += key[m][n]

                for m in range(M, M+N):
                    for n in range(M, M+N):
                        if newMatrix[m][n] != 1:
                            canMake = False

                if canMake:
                    return True

                for m in range(M):
                    for n in range(M):
                        newMatrix[i+m][j+n] -= key[m][n]

        key = rotateMatrix(key)

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))