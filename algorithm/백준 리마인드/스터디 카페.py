import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

timetable = []

for _ in range(M):
    s, e = map(int, input().split())
    timetable.append((s, e))

A.sort()

pf = [0]
for a in A:
    pf.append(pf[-1] + a)

maxValue = 0
minValue = 0
times = []
for ts, te in timetable:
    times.append((ts, 1))
    times.append((te+1, -1))

times.sort()

prev = 0
current = 0
count = 0
idx = 0

while idx < len(times):
    t, flag = times[idx]

    distance = t - prev
    maxValue += (pf[-1] - pf[-(1+count)]) * distance
    minValue += (pf[count]) * distance
    prev = t

    if flag == -1:
        count -= 1
        while idx+1 < len(times) and times[idx+1][0] == t and times[idx+1][1] == -1:
            idx += 1
            count -= 1

    else:
        count += 1
        while idx+1 < len(times) and times[idx+1][0] == t and times[idx+1][1] == 1:
            idx += 1
            count += 1

    idx += 1

print(minValue, maxValue)
