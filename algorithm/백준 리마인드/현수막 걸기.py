import bisect

N, M, R = map(int, input().split())

spots = list(map(int, input().split()))

sticks = list(map(int, input().split()))

lengths = set()

for i in range(N-1):
    for j in range(i+1, N):
        lengths.add(abs(spots[i] - spots[j]))

lengthList = list(lengths)
lengthList.sort()

maxValue = 0
MR = R * 2
for stick in sticks:
    target = MR / stick
    index = bisect.bisect_right(lengthList, target)
    if index != 0:
        temp = stick * lengthList[index-1]
        maxValue = max(maxValue, temp)

if maxValue == 0:
    print(-1)
else:
    print(maxValue / 2)

