import heapq
import bisect


def solution(n, t, m, timetable):
    startTime = 9 * 60

    table = []
    for time in timetable:
        tmp = list(map(int, time.split(":")))
        value = tmp[0] * 60 + tmp[1]
        heapq.heappush(table, value)

    latestTime = 0

    possibleStartTime = []
    for i in range(n):
        possibleStartTime.append(startTime + t * i)

    for i in range(len(possibleStartTime)):
        tmp = m
        timeList = []
        while table and table[0] <= possibleStartTime[i] and tmp > 0:
            tmp -= 1
            timeList.append(table[0])
            heapq.heappop(table)

        if tmp > 0:
            latestTime = max(latestTime, possibleStartTime[i])
        else:
            if i == len(possibleStartTime) - 1:
                ans = 0
                start = timeList[0] - 1
                end = timeList[-1]

                while start <= end:
                    print()
                    mid = (start + end) // 2

                index = bisect.bisect_right(timeList, mid)
                if index < len(timeList):
                    ans = mid
                    start = mid + 1
                else:
                    end = mid - 1

                latestTime = max(latestTime, ans)

            else:
                continue

    hour = latestTime // 60
    minute = latestTime % 60
    answer = "{:02d}".format(hour) + ":" + "{:02d}".format(minute)
    return answer

solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])