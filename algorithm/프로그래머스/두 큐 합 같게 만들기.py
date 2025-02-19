def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1 + sum2
    haveToMakeSum = total // 2
    startIndex = 0
    endIndex = len(queue1) - 1

    totalArray = queue1 + queue2
    totalSum = sum(queue1)
    answer = 0

    while startIndex <= endIndex and endIndex < len(totalArray):
        if totalSum > haveToMakeSum:
            totalSum -= totalArray[startIndex]
            startIndex += 1
            answer += 1
        elif totalSum < haveToMakeSum:
            endIndex += 1
            if endIndex < len(totalArray):
                totalSum += totalArray[endIndex]
                answer += 1
        else:
            return answer

    return -1

