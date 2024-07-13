from collections import deque

N, M = map(int, input().split())
balls = list(map(int, input().split()))

left = max(balls)
right = sum(balls)

ansList = []
ans = -1

while left <= right:
    mid = (left + right) // 2

    tempList = [False] * (len(balls))
    numberOfGroup = 0
    currentSum = 0
    for i in range(len(balls)):
        if currentSum + balls[i] <= mid:
            currentSum += balls[i]

        else:
            currentSum = balls[i]
            tempList[i] = True
            numberOfGroup += 1

    if currentSum > 0:
        numberOfGroup += 1

    if numberOfGroup <= M:
        ans = mid
        ansList = tempList
        right = mid - 1

    else:
        left = mid + 1

print(ans)
answer = deque()
previousIdx = 0
for k in range(len(ansList)):
    if ansList[k]:
        answer.append(k-previousIdx)
        previousIdx = k
answer.append(len(ansList) - previousIdx)

temp = len(answer)
tempArr = deque()

# print(answer)
while answer:
    t = answer.popleft()
    while t > 1 and temp < M:
        tempArr.append(1)
        t -= 1
        temp += 1
    if t != 0:
        tempArr.append(t)

print(*list(tempArr))
