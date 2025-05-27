N, K = map(int, input().split())
A = list(map(int, input().split()))

numberOfPossible = 0

remained = []

for i in range(len(A)):
    if A[i] >= K:
        numberOfPossible += 1
    else:
        remained.append(A[i])

remained.sort()

start = 0
end = len(remained) - 1

while start < end:
    if remained[start] + remained[end] >= K:
        numberOfPossible += 1
        start += 1
        end -= 1

    else:
        start += 1

print(numberOfPossible) if numberOfPossible > 0 else print(-1)