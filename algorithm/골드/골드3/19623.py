from heapq import *
import sys
input = sys.stdin.readline

N = int(input())

meeting = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
meeting.sort(key=lambda x: x[0])
proceeding, finished = [], []

for start, end, people in meeting:
    while proceeding and proceeding[0][0] <= start:
        heappush(finished, -heappop(proceeding)[1])

    if finished:
        heappush(proceeding, (end, people + -finished[0]))
    else:
        heappush(proceeding, (end, people))

while proceeding:
    heappush(finished, -heappop(proceeding)[1])

print(-finished[0])


