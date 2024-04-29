N, M = map(int, input().split())

A = []

for _ in range(N):
    l = list(map(int, input().split()))
    A.append(l)

M, K = map(int, input().split())

B = []

for _ in range(M):
    l = list(map(int, input().split()))
    B.append(l)

for n in range(N):
    Al = A[n]
    for k in range(K):
        sum = 0
        for m in range(M):
            sum += Al[m] * B[m][k]
        print(sum, end=' ')
    print()