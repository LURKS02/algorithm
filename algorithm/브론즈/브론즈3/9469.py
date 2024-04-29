P = int(input())

for i in range(P):
    N, D, A, B, F = map(float, input().split())
    h = D / (A + B)
    result = h * F
    print(f"{int(N)} {result}")