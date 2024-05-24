# N = 배열의 크기
# M = 나누는 구간 수
N, M = map(int, input().split())

# l = 배열의 각 수
l = list(map(int, input().split()))

answer = 10000
left, right = 0, max(l)

def check(mid):
    global answer
    group = 1
    nowMin = 10000
    nowMax = 0

    for i in range(N):
        nowMin = min(nowMin, l[i])
        nowMax = max(nowMax, l[i])

        if nowMax - nowMin > mid:
            group += 1
            nowMin = nowMax = l[i]

    return M >= group

while left <= right:
    mid = (left + right) // 2

    if check(mid):
        right = mid - 1
        answer = mid

    else:
        left = mid + 1

print(answer)