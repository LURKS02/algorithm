aa, ab = map(int, input().split())
ba, bb = map(int, input().split())

A = aa + bb
B = ab + ba
if (A < B):
    print(A)
else:
    print(B)