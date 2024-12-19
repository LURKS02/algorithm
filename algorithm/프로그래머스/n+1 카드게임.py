from collections import deque

def solution(coin, cards):
    answer = 0

    N = len(cards)
    haveToDrawFirst = N // 3

    pairIndex = [-1] * N
    for i in range(N):
        if pairIndex[i] == -1:
            target = N+1 - cards[i]
            for j in range(N):
                if cards[j] == target:
                    pairIndex[i] = j
                    pairIndex[j] = i

    totalStartScore = 0
    for i in range(haveToDrawFirst):
        card = cards[i]
        if pairIndex[i] < haveToDrawFirst:
            totalStartScore += 1
    totalStartScore = totalStartScore // 2

    rounds = [[] for _ in range((N - haveToDrawFirst) // 2)]

    for i in range(len(rounds)):
        firstCard = haveToDrawFirst + i * 2
        secondCard = haveToDrawFirst + i * 2 + 1

        if pairIndex[firstCard] == secondCard:
            rounds[i].append([1, 2])
        if pairIndex[firstCard] < haveToDrawFirst:
            rounds[i].append([1, 1])
        if pairIndex[secondCard] < haveToDrawFirst:
            rounds[i].append([1, 1])
        if haveToDrawFirst <= pairIndex[firstCard] < firstCard:
            rounds[i].append([1, 2])
        if haveToDrawFirst <= pairIndex[secondCard] < firstCard:
            rounds[i].append([1, 2])

    deq = deque()
    deq.append((1, totalStartScore, coin))

    answer = 0

    maxRound = (N - haveToDrawFirst) // 2 + 1
    visited = [[[False] * (coin+1) for _ in range(maxRound+1)] for _ in range(maxRound+1)]
    while deq:
        round, chance, currentCoin = deq.popleft()

        answer = max(answer, round)
        if round == maxRound:
            break

        if len(rounds[round-1]) == 2:
            if currentCoin >= rounds[round-1][0][1] + rounds[round-1][1][1]:
                if not visited[round+1][chance+1][currentCoin - rounds[round-1][0][1] - rounds[round-1][1][1]]:
                    visited[round + 1][chance + 1][currentCoin - rounds[round - 1][0][1] - rounds[round - 1][1][1]] = True
                    deq.append((round+1, chance+1, currentCoin - rounds[round-1][0][1] - rounds[round-1][1][1]))
            if currentCoin >= rounds[round-1][0][1]:
                if not visited[round+1][chance][currentCoin - rounds[round-1][0][1]]:
                    visited[round + 1][chance][currentCoin - rounds[round - 1][0][1]] = True
                    deq.append((round+1, chance, currentCoin - rounds[round-1][0][1]))
            if currentCoin >= rounds[round-1][1][1]:
                if not visited[round+1][chance][currentCoin - rounds[round-1][1][1]]:
                    visited[round + 1][chance][currentCoin - rounds[round - 1][1][1]] = True
                    deq.append((round+1, chance, currentCoin - rounds[round-1][1][1]))
        elif len(rounds[round-1]) == 1:
            if currentCoin >= rounds[round-1][0][1]:
                if not visited[round+1][chance][currentCoin - rounds[round-1][0][1]]:
                    visited[round + 1][chance][currentCoin - rounds[round - 1][0][1]] = True
                    deq.append((round + 1, chance, currentCoin - rounds[round-1][0][1]))

        if chance > 0:
            if not visited[round+1][chance-1][currentCoin]:
                visited[round + 1][chance - 1][currentCoin] = True
                deq.append((round+1, chance-1, currentCoin))

    return answer



solution(4, 	[3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4])
solution(3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12])
solution(2, 	[5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7])
solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
solution(0, [1, 2, 3, 4, 5, 6])

import random
numbers = list(range(1, 967))
random.shuffle(numbers)

solution(100, numbers)