import sys

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    k = a + b
    print(f'Case #{i + 1}: {k}')