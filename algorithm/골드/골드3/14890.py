import sys
input = sys.stdin.readline

N, L = map(int, input().rstrip().split())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().rstrip().split())))

canPass = 0
for i in range(N):
    start = matrix[i][0]
    canBridge = True

    used = [False for _ in range(N)]

    for j in range(1, N):
        if used[j]:
            continue

        if matrix[i][j] == start:
            continue

        if abs(matrix[i][j] - start) > 1:
            # print('1')
            canBridge = False
            break

        if matrix[i][j] > start and j >= L:

            usedCheck = False
            for k in range(1, L+1):
                if used[j-k] or start != matrix[i][j-k]:
                    usedCheck = True

            if not usedCheck:
                for k in range(1, L+1):
                    used[j-k] = True
                start = matrix[i][j]

            else:
                # print('2')
                canBridge = False
                break

        elif matrix[i][j] < start and j <= N-L:
            usedCheck = False
            for k in range(0, L):
                if used[j + k] or start - 1 != matrix[i][j+k]:
                    usedCheck = True

            if not usedCheck:
                for k in range(0, L):
                    used[j + k] = True
                start = matrix[i][j]

            else:
                # print('4')
                canBridge = False
                break
        else:
            # print(matrix[i][j], start)
            # print('5')
            canBridge = False
            break

    # print(canBridge)
    if canBridge:

        canPass += 1

# print(canPass)

for i in range(N):
    start = matrix[0][i]
    canBridge = True

    used = [False for _ in range(N)]

    for j in range(1, N):
        if used[j]:
            continue

        if matrix[j][i] == start:
            continue

        if abs(matrix[j][i] - start) > 1:
            # print('1')
            canBridge = False
            break

        if matrix[j][i] > start and j >= L:

            usedCheck = False
            for k in range(1, L+1):
                if used[j-k] or start != matrix[j-k][i]:
                    usedCheck = True

            if not usedCheck:
                for k in range(1, L+1):
                    used[j-k] = True
                start = matrix[j][i]

            else:
                # print('2')
                canBridge = False
                break

        elif matrix[j][i] < start and j <= N-L:
            usedCheck = False
            for k in range(0, L):
                if used[j + k] or start - 1 != matrix[j+k][i]:
                    usedCheck = True

            if not usedCheck:
                for k in range(0, L):
                    used[j + k] = True
                start = matrix[j][i]

            else:
                # print('4')
                canBridge = False
                break
        else:
            # print(matrix[i][j], start)
            # print('5')
            canBridge = False
            break

    # print(canBridge)
    if canBridge:

        canPass += 1

print(canPass)

