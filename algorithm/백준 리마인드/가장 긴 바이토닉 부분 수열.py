N = int(input())
A = list(map(int, input().split()))

upperA = [1] * len(A)
lowerA = [1] * len(A)

for i in range(1, len(A)):
    for j in range(i):
        if A[i] > A[j]:
            upperA[i] = max(upperA[i], upperA[j] + 1)

for i in range(len(A)-2, -1, -1):
    for j in range(len(A)-1, i, -1):
        if A[i] > A[j]:
            lowerA[i] = max(lowerA[i], lowerA[j] + 1)

maxLength = 1
for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        if A[i] != A[j]:
            maxLength = max(maxLength, upperA[i] + lowerA[j])

print(maxLength)