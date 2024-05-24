import sys
from collections import defaultdict
input = sys.stdin.readline

# order = 손님이 구매하고자 하는 크기 (2,000,000)
order = int(input())

# m = A 피자의 조각 수 (1,000)
# n = B 피자의 조각 수 (1,000)
m, n = map(int, input().split())

# A = A 피자의 조각 목록
# B = B 피자의 조각 목록
A = []
B = []

for _ in range(m):
    A.append(int(input()))
for _ in range(n):
    B.append(int(input()))

def findPizza(pizza):
    case = defaultdict(int)
    length = len(pizza)

    for i in range(length):
        temp = pizza[i:] + pizza[:i]
        pre = 0
        for num in temp:
            pre += num
            case[pre] += 1
    case[sum(pizza)] = 1
    return case

caseA = findPizza(A)
caseB = findPizza(B)

result = caseA.get(order, 0) + caseB.get(order, 0)

for num in caseA:
    if order - num in caseB:
        result += caseA[num] * caseB[order - num]

print(result)