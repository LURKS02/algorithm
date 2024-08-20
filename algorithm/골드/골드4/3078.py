from collections import defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

friendDict = defaultdict(list)

for i in range(N):
    rank = i
    name = input()
    nameLength = len(name)

    friendDict[nameLength].append(rank)

totalCount = 0

for key in friendDict.keys():
    friendList = sorted(friendDict[key])

    startIdx = 0
    endIdx = 0

    while startIdx <= endIdx and endIdx < len(friendList):
        if friendList[endIdx] - friendList[startIdx] <= K:
            totalCount += endIdx - startIdx
            endIdx += 1

        else:
            startIdx += 1

print(totalCount)




