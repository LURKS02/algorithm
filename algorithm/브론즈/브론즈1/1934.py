import math

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(A * B // math.gcd(A, B))