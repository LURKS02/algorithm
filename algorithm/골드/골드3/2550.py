import bisect

N = int(input())
switches = list(map(int, input().split()))
bulbs = list(map(int, input().split()))

# dp[전구 번호] = 2번 배열에서의 위치
dp = [0 for _ in range(N+1)]

for idx, bulb in enumerate(bulbs):
    dp[bulb] = idx + 1

# 맞는 스위치의 목록
LIS = []
idx = []

for switch in switches:
    now = dp[switch]
    if len(LIS) == 0 or LIS[-1] < now:
        idx.append(len(LIS))
        LIS.append(now)
    else:
        cur = bisect.bisect_left(LIS, now)
        if len(LIS) == cur:
            LIS.append(now)
        else:
            LIS[cur] = now
        idx.append(cur)

print(len(LIS))

answer = []
pos = max(idx)
for v in idx[::-1]:
    N -= 1
    if pos == v:
        answer.append(switches[N])
        pos -= 1

print(*sorted(answer))