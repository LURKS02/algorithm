import heapq

def solution(cards):
    visited = [False] * (len(cards))
    heap = []

    for i in range(len(cards)):
        currentIndex = i
        count = 0
        while True:
            if not visited[currentIndex]:
                visited[currentIndex] = True
                count += 1
                currentIndex = cards[currentIndex]-1
            else:
                break
        heapq.heappush(heap, -count)

    temp1 = -heapq.heappop(heap)
    temp2 = -heapq.heappop(heap)
    return (temp1 * temp2)

solution([8,6,3,7,2,5,1,4])