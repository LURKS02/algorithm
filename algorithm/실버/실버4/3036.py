import math

N = int(input())

circles = list(map(int, input().split()))

m = circles[0]

for n in circles[1:]:
    big = math.gcd(m, n)
    print(m // big, end='')
    print('/',end='')
    print(n // big, end='')
    print()