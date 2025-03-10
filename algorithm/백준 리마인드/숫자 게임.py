import sys
input = sys.stdin.readline

N = int(input())

A = [0] * 101
B = [0] * 101

for _ in range(N):
    a, b = map(int, input().split())
    A[a] += 1
    B[b] += 1
    answer = 0

    tempA = A[:]
    tempB = B[:]
    aIndex = 0
    bIndex = 100

    while aIndex <= 100 and bIndex >= 0:
        if tempA[aIndex] == 0:
            aIndex += 1
            continue
        if tempB[bIndex] == 0:
            bIndex -= 1
            continue

        if tempA[aIndex] >= tempB[bIndex]:
            answer = max(answer, aIndex + bIndex)
            tempA[aIndex] -= tempB[bIndex]
            tempB[bIndex] = 0

        else:
            answer = max(answer, aIndex + bIndex)
            tempB[bIndex] -= tempA[aIndex]
            tempA[aIndex] = 0

    print(answer)