import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

seat = [k for k in range(K)]
heap = []
time = 0
answer = 0
idx = 1

for _ in range(N):
    id, w = map(int, input().split())

    if seat:
        s = heapq.heappop(seat)
        heapq.heappush(heap, (time + w, -s, id))

    else:
        time = heap[0][0]

        while heap and heap[0][0] == time:
            end, s, outID = heapq.heappop(heap)
            heapq.heappush(seat, -s)
            answer += outID * idx
            idx += 1

        s = heapq.heappop(seat)
        heapq.heappush(heap, (time + w, -s, id))

while heap:
    end, s, outID = heapq.heappop(heap)
    answer += outID * idx
    idx += 1

print(answer)
