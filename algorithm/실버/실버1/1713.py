N = int(input())
recomNum = int(input())
l = list(map(int, input().split()))

presented = set()
passedDays = [0] * 101
recommendation = [0] * 101

for student in l:
    if len(presented) == N and student not in presented:
        minRecommended = []
        minRecommendCount = float('inf')
        for p in presented:
            if minRecommendCount > recommendation[p]:
                minRecommendCount = recommendation[p]
                minRecommended = [p]
            elif minRecommendCount == recommendation[p]:
                minRecommended.append(p)
        if len(minRecommended) == 1:
            p = minRecommended[0]
            presented.remove(minRecommended[0])
            passedDays[p] = 0
            recommendation[p] = 0
        else:
            maxPassedCount = -float('inf')
            maxPassed = -1

            for m in minRecommended:
                if passedDays[m] > maxPassedCount:
                    maxPassedCount = passedDays[m]
                    maxPassed = m
            presented.remove(maxPassed)
            passedDays[maxPassed] = 0
            recommendation[maxPassed] = 0

        presented.add(student)
        recommendation[student] += 1

    else:
        recommendation[student] += 1
        presented.add(student)

    for i in range(101):
        if recommendation[i] > 0:
            passedDays[i] += 1

    # print(presented)
    # print(recommendation)
    # print(passedDays)

print(*sorted(list(presented)))