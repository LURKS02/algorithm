N = int(input())

A = list(map(int, input().split()))
A.sort()
answer = 0

for i in range(N):
    num = A[i]
    isGood = False

    left = 0
    right = N-1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        if A[left] + A[right] < num:
            left += 1
        elif A[left] + A[right] > num:
            right -= 1
        else:
            isGood = True
            break

    if isGood:
        answer += 1

print(answer)