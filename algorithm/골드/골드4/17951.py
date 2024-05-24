# N = 시험지의 수
# K = 그룹의 수
N, K = map(int, input().split())

# 각 시험지의 점수
scores = list(map(int, input().split()))

answer = 0

left, right = 0, int(1e5) * 20 + 1

while left <= right:
    mid = (left + right) // 2

    group = 0
    groupScore = 0

    for score in scores:
        groupScore += score
        if groupScore >= mid:
            group += 1
            groupScore = 0

    if group >= K:
        answer = mid
        left = mid + 1

    else:
        right = mid - 1

print(answer)