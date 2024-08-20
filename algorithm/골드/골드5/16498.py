from bisect import bisect_left, bisect_right

A, B, C = map(int, input().split())

answer = 2000000000

ACards = sorted(list(map(int, input().split())))
BCards = sorted(list(map(int, input().split())))
CCards = sorted(list(map(int, input().split())))

def search(a, b, c):
    global answer

    for i in a:
        for j in b:
            maxNum = max(i, j)
            minNum = min(i, j)

            maxIndex = bisect_right(c, maxNum) - 1
            minIndex = bisect_left(c, minNum)

            if 0 <= minIndex <= maxIndex < len(c):
                answer = min(answer, abs(maxNum - minNum))

search(ACards, BCards, CCards)
search(BCards, CCards, ACards)
search(ACards, CCards, BCards)

print(answer)