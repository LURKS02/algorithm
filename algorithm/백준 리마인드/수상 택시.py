import sys
input = sys.stdin.readline

N, M = map(int, input().split())

times = []

for _ in range(N):
    start, end = map(int, input().split())
    times.append((start, end))

times.sort(key=lambda x: (-x[0], x[1]))

startTime = M
maxTime = M
total = 0

for time in times:
    startT, endT = time
    if startT <= endT:
        continue
    else:
        if maxTime <= endT:
            continue
        elif maxTime <= startT and maxTime > endT:
            if (startTime - maxTime) * 2 + (startT - endT) * 2 + (startTime - startT) < (startTime - endT) * 2:
                total += (startTime - maxTime) * 2
                startTime = startT
                maxTime = endT
            else:
                maxTime = endT
        else:
            total += (startTime - maxTime) * 2
            startTime = startT
            maxTime = endT

total += (startTime - maxTime) * 2
total += M
print(total)
