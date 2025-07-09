N, T = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

dp = [0] * 200001

def calc(num):
    for i in range(N):
        dp[i] = arr[i]

    if num == 0:
        return False

    for i in range(N):
        if i < num:
            if dp[i] >= T:
                dp[i] = arr[i] + 1
            else:
                dp[i] = T + 1
        else:
            if dp[i-num] > arr[i]:
                return False
            if dp[i-num] + T <= arr[i] + 1:
                dp[i] = arr[i] + 1
            else:
                dp[i] = dp[i-num] + T

    return True


def bs():
    left = 1
    right = 200000
    mid = (left + right) // 2

    while left < right:
        if calc(mid):
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2

    if not calc(mid):
        mid += 1
    return mid

print(bs())