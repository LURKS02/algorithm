
N, M, K = map(int, input().split())
notsolved = M * (K - 1)
min = N - notsolved - M
max = N - notsolved - 1

if min < 0:
    min = 0
print(min, max, end= ' ')