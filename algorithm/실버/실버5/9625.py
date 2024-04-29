K = int(input())

def countAB(K):
    A, B = 1, 0

    for _ in range(K):
        A, B = B, A + B

    return A, B

A, B = countAB(K)

print(A, B, end=' ')
