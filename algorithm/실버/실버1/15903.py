import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))
sum = sum(cards)
heapq.heapify(cards)

for i in range(m):
    smallest1 = heapq.heappop(cards)
    smallest2 = heapq.heappop(cards)
    value = smallest1 + smallest2

    heapq.heappush(cards, value)
    heapq.heappush(cards, value)
    sum += value

print(sum)

