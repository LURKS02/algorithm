N, M = map(int, input().split())

rides = list(map(int, input().split()))

start = 0
end = 60000000000
ans = 0

while start <= end:
    mid = (start + end) // 2

    rided = 0
    for ride in rides:
        rided += 1
        if mid >= ride:
            rided += mid // ride

    if rided < N:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid

if N <= M:
    print(N)
else:
    zeros = []
    for i in range(len(rides)):
        if ans % rides[i] == 0:
            zeros.append(i)

    temp = ans - 1
    total = 0
    for i in range(len(rides)):
        total += temp // rides[i] + 1
    haveTo = N - total

    print(zeros[haveTo-1] + 1)


# f(t) = t만큼의 시간이 지났을 때, 몇 명이 놀이기구에 탑승했는가?