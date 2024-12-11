N, x = map(int, input().split())
p = list(map(int, input().split()))

buyCount = N-2
p.append(x)
p.sort()

homeIndex = p.index(x)
minDistance = float('inf')

leftRange = max(0, homeIndex - buyCount)
rightRange = min(len(p)-buyCount, homeIndex+1)
for i in range(leftRange, rightRange):
    distance = p[i + buyCount] - p[i] + min(p[i+buyCount] - p[homeIndex], p[homeIndex] - p[i])
    minDistance = min(minDistance, distance)

print(minDistance)