import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
lectures = [tuple(map(int, input().rstrip().split())) for _ in range(N)]

lectures.sort(key=lambda x: x[0])

rooms = []
heapq.heappush(rooms, lectures[0][1])

for i in range(1, N):
    if lectures[i][0] >= rooms[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, lectures[i][1])

print(len(rooms))