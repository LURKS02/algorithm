def getPay(electronic):
    if electronic <= 100:
        return electronic * 2

    elif electronic <= 10000:
        return 2*100 + (electronic - 100) * 3

    elif electronic <= 1000000:
        return 2*100 + 3*9900 + (electronic - 10000) * 5

    else:
        return 2*100 + 3*9900 + 5*990000 + (electronic - 1000000) * 7

def getUsedElectronic(pay):

    if pay <= 200:
        return pay // 2

    elif pay <= 30000:
        return 100 + (pay - 2*100) // 3

    elif pay <= 5000000:
        return 100 + 9900 + (pay - 2*100 - 3*9900) // 5

    else:
        return 100 + 9900 + 990000 + (pay - 2*100 - 3*9900 - 5*990000) // 7

while True:
    # A = 이웃의 사용량 + 내 사용량 요금 (1,000,000,000)
    # B = 이웃과의 요금 차이 절댓값 (1,000,000,000)
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        exit(0)

    totalUsed = getUsedElectronic(A)

    # 상근이의 사용량 구하기
    left = 0
    right = totalUsed
    usedElectronic = 0

    answerPay = 0

    while left <= right:
        mid = (left + right) // 2

        myElectronic = mid
        otherElectronic = totalUsed - myElectronic

        myPay = getPay(myElectronic)
        otherPay = getPay(otherElectronic)

        if otherPay - myPay <= B:
            answerPay = myPay
            right = mid - 1

        else:
            left = mid + 1

    print(answerPay)

