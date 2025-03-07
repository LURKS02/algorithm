import heapq

N = int(input())
A = list(input().split())

start = ''.join(A)
numA = list(map(int, A))
sortedA = sorted(numA)
stredA = list(map(str, sortedA))

target = ''.join(stredA)

commands = []

M = int(input())
for _ in range(M):
    l, r, c = map(int, input().split())
    commands.append((l-1, r-1, c))

heap = []
heap.append((0, A))
cost = dict()
cost[start] = 0

while heap:
    count, arr = heapq.heappop(heap)

    if arr == stredA:
        print(count)
        exit(0)

    for a, b, value in commands:
        tempArr = arr[:]
        tempArr[a], tempArr[b] = tempArr[b], tempArr[a]
        newString = ''.join(tempArr)
        newCost = count + value

        if newString not in cost:
            cost[newString] = newCost
            heapq.heappush(heap, (newCost, tempArr))

        elif newCost < cost[newString]:
            cost[newString] = newCost
            heapq.heappush(heap, (newCost, tempArr))

print(-1)

