import math
def solution(n, stations, w):
    answer = 0
    idx = 1
    for station in stations:
        start = station - w
        end = station + w
        if start < 1:
            start = 1
        if end > n:
            end = n
        answer += math.ceil((start - idx) / (2 * w + 1))
        idx = end + 1

    if n - idx >= 0:
        answer += math.ceil((n - idx + 1) / (2 * w + 1))

    return answer