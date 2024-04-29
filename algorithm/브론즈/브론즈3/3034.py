import math

N, W, H = map(int, input().split())
max = math.sqrt(pow(W, 2) + pow(H, 2))
for _ in range(N):
    L = int(input())
    if L <= max:
        print("DA")
    else:
        print('NE')