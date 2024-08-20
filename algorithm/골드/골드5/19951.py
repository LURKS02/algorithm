import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
H = list(map(int, input().rstrip().split()))

pf = [0] * N

for _ in range(M):
    a, b, k = map(int, input().rstrip().split())
    pf[a-1] += k
    if b < N:
        pf[b] += k * (-1)

for i in range(0, N-1):
    pf[i+1] += pf[i]

for i in range(0, N):
    H[i] += pf[i]

print(*H)