import heapq

N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))
cards.sort()

if N == 1:
    print(0)
    exit(0)

answer = 0

while len(cards) > 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    answer += (card1 + card2)
    heapq.heappush(cards, card1 + card2)

print(answer)