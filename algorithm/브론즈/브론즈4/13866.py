a, b, c, d = map(int, input().split())
A = a + d
B = b + c

if A > B:
    print(A - B)
else:
    print(B - A)