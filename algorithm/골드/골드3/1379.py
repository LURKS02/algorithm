import sys
import heapq

input = sys.stdin.readline

# N = 강의의 개수 (100,000)
N = int(input().rstrip())

classes = []

for _ in range(N):
    classNum, startTime, endTime = map(int, input().rstrip().split())
    classNum -= 1
    classes.append((classNum, startTime, endTime))

lectures = [-1 for _ in range(N)]
classes.sort(key=lambda x: (x[1], x[2]))
# print(classes)
room = []

for i in range(0, N):
    heapq.heappush(room, i)

# print(room)

minHeap = []

for c in classes:
    # print(c)
    while minHeap and minHeap[0][0] <= c[1]:
        end, r = heapq.heappop(minHeap)
        heapq.heappush(room, r)

    r = heapq.heappop(room)
    heapq.heappush(minHeap, [c[2], r])
    lectures[c[0]] = r
    # print(lectures)

print(max(lectures)+1)
for l in lectures:
    print(l+1)