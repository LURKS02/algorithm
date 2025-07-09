import heapq
import sys
input = sys.stdin.readline

N = int(input())
numbers = []
currentValue = 0
ans = 0

for _ in range(N):
    line = list(map(int, input().split()))

    if line[0] == 1:
        numbers.append(line[1])

    else:
        numbers.append(currentValue)
        numbers.sort()
        idx = -1

        for i in range(len(numbers)):
            if numbers[i] == currentValue:
                idx = i

        start = idx
        end = idx

        while True:
            leftDistance = abs(numbers[start-1] - currentValue) if start > 0 else float('inf')
            rightDistance = abs(numbers[end+1] - currentValue) if end < len(numbers)-1 else float('inf')

            if leftDistance == float('inf') and rightDistance == float('inf'):
                numbers = []
                break

            if leftDistance <= rightDistance:
                ans += leftDistance
                currentValue = numbers[start-1]
                start -= 1
            else:
                ans += rightDistance
                currentValue = numbers[end+1]
                end += 1

print(ans)