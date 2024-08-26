N, K, C = map(int, input().split())
times = list(map(int, input().split()))

answer = float('inf')

def getTime(times, K):
    start = 1
    end = max(times) * K
    ans = 1

    while start <= end:
        mid = (start + end) // 2
        # print(start, end)
        # print(mid)

        total = 0
        for i in range(len(times)):
            total += mid // times[i]

        if total >= K:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    # print("ans", ans)
    return ans

def backtracking(care):
    global answer
    answer = min(answer, getTime(times, K))
    if care == 0 or sum(times) == len(times):
        return

    for i in range(N):
        if times[i] > 1:
            times[i] -= 1
            backtracking(care - 1)
            times[i] += 1

backtracking(C)

print(answer)