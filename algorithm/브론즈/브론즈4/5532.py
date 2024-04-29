l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a % c == 0):
    A = a // c
else:
    A = a // c + 1

if (b % d == 0):
    B = b // d
else:
    B = b // d + 1

if (A > B):
    print(l-A)
else:
    print(l-B)