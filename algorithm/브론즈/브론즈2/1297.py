import math

D, H, W = map(int, input().split())

a = math.sqrt(pow(D, 2) / (pow(H, 2) + pow(W, 2)))

h = math.floor(a * H)
w = math.floor(a * W)
print(h, w, end= ' ')