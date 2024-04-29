def gcd(A, B):
    while B != 0:
        A, B = B, A % B
    return A

A, B = map(int, input().split())

if A > B:
    print(gcd(A, B) * '1')
else:
    print(gcd(B, A) * '1')