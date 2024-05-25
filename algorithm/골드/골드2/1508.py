# N = 트랙의 길이 (1,000,000)
# M = 심판의 수 (50)
# K = 심판이 위치할 수 있는 장소의 수 (50)
N, M, K = map(int, input().split())

# spots = 심판이 위치할 수 있는 장소 리스트 (0 ~ 1,000,000)
spots = list(map(int, input().split()))

left = 1
right = spots[-1] - spots[0]

while left <= right:
    mid = (left + right) // 2

    cnt = 1
    now = spots[0]

    for i in range(1, len(spots)):
        if spots[i] - now >= mid:
            cnt += 1
            now = spots[i]

    if cnt < M:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

ans = '1'
cnt = 1
now = spots[0]

# print(result)

for i in range(1, len(spots)):
    if spots[i] - now >= result and cnt < M:
        ans += '1'
        cnt += 1
        now = spots[i]
    else:
        ans += '0'

print(ans)

