N = int(input())

lines = []

for _ in range(N):
    x, y = map(int, input().split())
    lines.append((x, y))

curX, curY = lines[0]
totalLength = 0

for i in range(1, len(lines)):
    if curX <= lines[i][0] <= curY:
        curY = max(curY, lines[i][1])
    else:
        totalLength += (curY - curX)
        curX = lines[i][0]
        curY = lines[i][1]

totalLength += (curY - curX)

print(totalLength)