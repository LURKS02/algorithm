import heapq

# N = 주문의 개수 (100,000)
# X = 남은 시간 (1,000,000,000)
N, X = map(int, input().split())

# times = 각 선물의 공정 시간
times = list(map(int, input().split()))

left = 1
right = 100000

ans = 1

while left <= right:
    mid = (left + right) // 2

    machines = [0] * mid

    for time in times:
        leastTimeMachine = heapq.heappop(machines)
        heapq.heappush(machines, leastTimeMachine + time)

    biggestTime = max(machines)

    if biggestTime <= X:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)