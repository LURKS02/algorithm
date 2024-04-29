def flip(matrix, x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            matrix[i][j] = 1 - matrix[i][j]
def is_same(A, B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != B[i][j]:
                return False
    return True

def solve(A, B):
    N, M = len(A), len(A[0])
    count = 0

    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                flip(A, i, j)
                count += 1
    if is_same(A, B):
        return count
    else:
        return -1

N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]

if N < 3 or M < 3:
    if is_same(A, B):
        print(0)
    else:
        print(-1)
else:
    print(solve(A, B))