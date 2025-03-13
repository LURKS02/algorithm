from itertools import combinations

L, C = map(int, input().split())

alpabets = list(input().split())

answer = []
for comb in combinations(alpabets, L):
    sortedComb = sorted(comb)
    mCount = 0

    for i in range(len(sortedComb)):
        if sortedComb[i] in ["a", "e", "i", "o", "u"]:
            mCount += 1

    if mCount >= 1 and len(sortedComb) - mCount >= 2:
        answer.append("".join(sortedComb))

answer.sort()
for a in answer:
    print(a)