import sys
input = sys.stdin.readline

N = int(input())

buildings = []
for _ in range(N):
    x, y = map(int, input().split())
    buildings.append((x, y))
buildings.sort()

buildings = [(0, 0)] + buildings

dp = [float('inf')] * (N+1)

dp[0] = 0

for i in range(1, N+1):
    up = 0
    for j in range(i, 0, -1):
        up = max(up, abs(buildings[j][1]))
        square = max(buildings[i][0] - buildings[j][0], up * 2)
        # print(i, j)
        # print(up, square)
        dp[i] = min(dp[i], dp[j-1] + square)
# print(dp)
print(dp[-1])