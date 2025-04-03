import heapq

N = int(input())
bridge = list(map(int, input().split()))
cost = list(map(int, input().split()))

heap = []

heap.append(cost[0])

totalCost = 0
for i in range(len(bridge)):
    totalCost += heap[0] * bridge[i]
    heapq.heappush(heap, cost[i+1])

print(totalCost)
