import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nodeInfo = [[0, 0] for _ in range(200001)]

rails = []

for i in range(N):
    x, y = map(int, input().split())
    nodeInfo[i+1] = [x, y]

for _ in range(M):
    u, v, c = map(int, input().split())
    ux, uy = nodeInfo[u]
    vx, vy = nodeInfo[v]

    if uy <= vy:
        rails.append((uy, c))
        rails.append((vy, -c))
    else:
        rails.append((vy, c))
        rails.append((uy, -c))

position = 0
val = 0
maxVal = -float('inf')

rails.sort(key=lambda x: (x[0], -x[1]))

idx = 0
while idx < len(rails):
    while idx < len(rails) and rails[idx][0] == position and rails[idx][1] > 0:
        val += rails[idx][1]
        idx += 1

    maxVal = max(maxVal, val)

    while idx < len(rails) and rails[idx][0] == position:
        val += rails[idx][1]
        idx += 1

    if idx < len(rails):
        position = rails[idx][0]

print(maxVal)