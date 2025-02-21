def solution(lines):
    times = []

    for line in lines:
        _, time, duration = line.split(" ")

        hourString, minuteString, secondString = time.split(":")
        hour = int(hourString) * 60 * 60 * 1000
        minute = int(minuteString) * 60 * 1000
        second = int(float(secondString) * 1000)
        totalSecond = hour + minute + second

        d = int(float(duration[:-1]) * 1000)
        startTime = totalSecond - d + 1
        times.append((startTime, totalSecond))

    maxPerformance = 0

    for startTime, endTime in times:
        p = 0
        startSecond = startTime
        endSecond = startTime + 1000

        for s, e in times:
            if startSecond <= s < endSecond or startSecond <= e < endSecond or (s < startSecond and e >= endSecond):
                p += 1
        maxPerformance = max(maxPerformance, p)

        p = 0
        startSecond = endTime
        endSecond = endTime + 1000

        for s, e in times:
            if startSecond <= s < endSecond or startSecond <= e < endSecond or (s < startSecond and e >= endSecond):
                p += 1
        maxPerformance = max(maxPerformance, p)

    return maxPerformance


solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])