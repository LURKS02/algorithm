M = int(input())

A = 1

for i in range(M):
    a, b = map(int, input().split())
    if a == A:
        A = b
    elif b == A:
        A = a

print(A)