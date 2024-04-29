import math

A, B = map(int, input().split())
gcdValue = math.gcd(A, B)
print(A * B // gcdValue)