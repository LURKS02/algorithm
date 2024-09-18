import sys

input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))

start = 0
e = float('inf')
steak = 0

for mid in range(1, N):
    leftSum = students[mid-1]
    rightSum = students[mid]
    left = mid-1
    right = mid

    while True:
        diff = abs(leftSum - rightSum)
        if diff == e:
            steak = max(steak, leftSum + rightSum)
        elif diff < e:
            e = diff
            steak = leftSum + rightSum

        if leftSum < rightSum:
            if left == 0:
                break
            left -= 1
            leftSum += students[left]
        elif leftSum > rightSum:
            if right == N-1:
                break
            right += 1
            rightSum += students[right]
        else:
            if left == 0 or right == N-1:
                break
            left -= 1
            right += 1
            leftSum += students[left]
            rightSum += students[right]

print(steak)