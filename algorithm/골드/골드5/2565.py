N = int(input())

inputs = []

for _ in range(N):
    inputs.append(tuple(map(int, input().split())))

inputs.sort()

collectedInputs = [b for a, b in inputs]

lis = [collectedInputs[0]]

for i in range(1, len(collectedInputs)):
    if collectedInputs[i] > lis[-1]:
        lis.append(collectedInputs[i])
    else:
        left, right = 0, len(lis) - 1
        while left <= right:
            mid = (left + right) // 2
            if lis[mid] < collectedInputs[i]:
                left = mid + 1
            else:
                right = mid - 1
        lis[left] = collectedInputs[i]

print(N - len(lis))
