import heapq

N = int(input())

plusQ = []
minusQ = []
haveZero = False

for _ in range(N):
    num = int(input())
    if num > 0:
        heapq.heappush(plusQ, -num)
    elif num < 0:
        heapq.heappush(minusQ, num)
    else:
        haveZero = True

sum = 0

while(len(plusQ) > 1):
    firstNum = -heapq.heappop(plusQ)
    secondNum = -heapq.heappop(plusQ)
    if firstNum == 1 or secondNum == 1:
        sum += firstNum
        sum += secondNum
    else:
        sum += firstNum * secondNum

while(len(minusQ) > 1):
    firstNum = heapq.heappop(minusQ)
    secondNum = heapq.heappop(minusQ)
    sum += firstNum * secondNum

if len(plusQ) == 1 and len(minusQ) == 1:
    pNum = -heapq.heappop(plusQ)
    mNum = heapq.heappop(minusQ)

    sumNum = pNum + mNum
    doubleNum = pNum * mNum

    if haveZero:
        sum += max(sumNum, doubleNum, pNum)
    else:
        sum += max(sumNum, doubleNum)

elif len(plusQ) == 1:
    sum += -heapq.heappop(plusQ)
elif len(minusQ) == 1:
    if not haveZero:
        sum += heapq.heappop(minusQ)

print(sum)