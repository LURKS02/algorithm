N, M = map(int, input().split())

jewels = [int(input()) for _ in range(N)]

pf = [0] * (N+1)
minVal = [float('inf')] * (N+1)
res = 0

for i in range(N):
    pf[i+1] = pf[i] + jewels[i]
    minVal[i+1] = min(pf[i+1], minVal[i])
    if i >= M-1:
       res = max(res, max(pf[i+1], pf[i+1] - minVal[i+1-M]))

print(res)