N = int(input())

timetable = []

for _ in range(N):
    T, A, B = map(int, input().split())
    timetable.append((T, A+1000, B+1000))

timetable.sort()

dp = [[float('inf')] * 2001 for _ in range(N+1)]
dp[0][1000] = 0

currentTime = 0
for i in range(len(timetable)):
    t, a, b = timetable[i]

    for k in range(2001):
        if dp[i][k] != float('inf'):
            possibleTime = t - currentTime
            for temp in range(-possibleTime, possibleTime+1, 1):
                newPosition = k + temp
                if newPosition >= 0 and newPosition <= a or newPosition >= b:
                    dp[i+1][newPosition] = min(dp[i+1][newPosition], dp[i][k] + abs(temp))

    currentTime = t

minVal = min(dp[N])

if minVal == float('inf'):
    print(-1)
else:
    print(minVal)

