a, b = map(int, input().split())

A = (a + b)//2
B = a - A

if (A + B != a or A - B != b):
    print(-1)
elif (A < 0 or B < 0):
    print(-1)
else:
    print(A, B, end= ' ')