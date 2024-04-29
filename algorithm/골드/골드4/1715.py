import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
nums = []
for _ in range(N):
    nums.append(int(input().rstrip()))

heapq.heapify(nums)
totalComp = 0

while len(nums) > 1:
    smallest = heapq.heappop(nums)
    secondSmallest = heapq.heappop(nums)
    newBundle = smallest + secondSmallest
    heapq.heappush(nums, newBundle)
    totalComp += newBundle

print(totalComp)