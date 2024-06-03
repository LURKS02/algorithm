import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

sumDict = {0: 1}

value = 0
answer = 0

for num in A:
    value += num

    if value - K in sumDict.keys():
        answer += sumDict[value - K]

    sumDict[value] = sumDict.get(value, 0) + 1

print(answer)