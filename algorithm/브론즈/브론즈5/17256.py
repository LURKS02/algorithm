A = list(map(int, input().split()))
C = list(map(int, input().split()))

Bx = C[0] - A[2]
By = C[1] // A[1]
Bz = C[2] - A[0]

print(Bx, By, Bz, end=' ')