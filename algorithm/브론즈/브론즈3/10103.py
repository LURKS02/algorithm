N = int(input())

A, B = 100, 100

for i in range(N):
    a, b = map(int, input().split())
    if a > b:
        B = B - a
    elif a < b:
        A = A - b


print(A)
print(B)


