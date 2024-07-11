import sys
input = sys.stdin.readline
INF = float('inf')

N = int(input().rstrip())
sx, sy = map(int, input().rstrip().split())
cakes = [(sx, sy)]

for _ in range(N):
    x, y = map(int, input().rstrip().split())
    cakes.append((x, y))
dist = [[INF] * 5 for _ in range(N+1)]

for k in range(4):
    dist[0][k] = 1
dist[0][4] = 0

dx = [0, 0, -1, 1, 0]
dy = [1, -1, 0, 0, 0]

for i in range(1, N+1):
    for j in range(5):
        x, y = cakes[i][0] + dx[j], cakes[i][1] + dy[j]

        for k in range(5):
            ex, ey = cakes[i-1][0] + dx[k], cakes[i-1][1] + dy[k]
            dist[i][j] = min(dist[i][j], abs(ex-x) + abs(ey-y) + dist[i-1][k])

print(min(dist[-1]))
