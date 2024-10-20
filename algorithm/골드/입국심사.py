def solution(n, times):
    minTime = min(times)
    left = minTime
    right = minTime * n
    answer = minTime * n
    while left <= right:
        mid = (left + right) // 2

        totalPerson = sum([mid // p for p in times])

        if totalPerson >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer