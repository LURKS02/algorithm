import sys
import bisect

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
points = []

for _ in range(N):
    x, y = map(int, input().rstrip().split())
    points.append((x, y))

commands = list(input().rstrip())

xPoints = sorted([x for x, y in points])
yPoints = sorted([y for x, y in points])

xPS = [0] * (N+1)
yPS = [0] * (N+1)

for i in range(1, N+1):
    xPS[i] = xPS[i-1] + xPoints[i-1]
    yPS[i] = yPS[i-1] + yPoints[i-1]

currentX, currentY = 0, 0
result = []

for command in commands:
    if command == "S":
        currentY += 1
    elif command == "J":
        currentY -= 1
    elif command == "I":
        currentX += 1
    elif command == "Z":
        currentX -= 1

    xIdx = bisect.bisect_left(xPoints, currentX)
    leftXSum = xPS[xIdx]
    rightXSum = xPS[N] - leftXSum

    leftCount = xIdx
    rightCount = N - xIdx

    xDistance = (currentX * leftCount - leftXSum) + (rightXSum - currentX * rightCount)

    yIdx = bisect.bisect_left(yPoints, currentY) - 1
    leftYSum = yPS[yIdx+1]
    rightYSum = yPS[N] - leftYSum

    leftCount = yIdx+1
    rightCount = N - leftCount

    yDistance = (currentY * leftCount - leftYSum) + (rightYSum - currentY * rightCount)

    result.append(xDistance + yDistance)

for r in result:
    print(r)