P = int(input())

l = []

A = 0
B = 0
C = 0
D = 0

for i in range(P):
    g, c, n = map(int, input().split())
    if g == 1:
        D += 1
    else:
        if c == 1 or c == 2:
            A += 1

        elif c == 3:
            B += 1

        else:
            C += 1


print(A)
print(B)
print(C)
print(D)
