import sys
input = sys.stdin.readline

N, T = map(int, input().split())

timetable = [0 for _ in range(100002)]

for _ in range(N):
    K = int(input())

    for _ in range(K):
        s, e = map(int, input().split())

        timetable[s+1] += 1
        timetable[e+1] -= 1

for i in range(100001):
    timetable[i+1] += timetable[i]

for i in range(100001):
    timetable[i+1] += timetable[i]

maxValue = -1
startIdx = 0
endIdx = 0

for i in range(T, 100002):
    value = timetable[i] - timetable[i-T]
    if value > maxValue:
        maxValue = value
        startIdx = i-T
        endIdx = i

print(startIdx, endIdx)