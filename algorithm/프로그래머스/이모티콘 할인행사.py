from itertools import product

def solution(users, emoticons):
    discountPercents = [10, 20, 30, 40]

    maxUserCount = 0
    maxCost = 0

    for p in product(discountPercents, repeat=len(emoticons)):
        productList = list(p)
        productUserCount = 0
        productCost = 0

        for user in users:
            userPercent = user[0]
            userInvest = user[1]
            totalCost = 0
            for i in range(len(emoticons)):
                if productList[i] >= userPercent:
                    totalCost += emoticons[i] * (100 - productList[i]) // 100

            if totalCost >= userInvest:
                productUserCount += 1
            else:
                productCost += totalCost

        if maxUserCount < productUserCount:
            maxUserCount = productUserCount
            maxCost = productCost
        elif maxUserCount == productUserCount and maxCost < productCost:
            maxCost = productCost

    return [maxUserCount, maxCost]

# print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))