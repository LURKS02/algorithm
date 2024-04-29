N, W, H, L = map(int, input().split())

a = W // L
b = H // L
total = a * b
print(min(N, total))