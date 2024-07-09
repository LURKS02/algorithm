N = int(input())
l = list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(1, N+1):
    # i번째 학생을 새 조로 추가하는 경우
    dp[i] = dp[i-1]
    minVal, maxVal = l[i-1], l[i-1]

    j = i-2

    while j >= 0 and (l[j] < minVal or l[j] > maxVal):
        minVal, maxVal = min(l[j], minVal), max(l[j], maxVal)
        dp[i] = max(dp[i], dp[j] + maxVal - minVal)
        j -= 1

print(dp[-1])
