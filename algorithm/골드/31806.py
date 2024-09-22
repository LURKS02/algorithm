import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
intervals = defaultdict(list)

for _ in range(N):
    l, r, c = map(int, input().split())
    intervals[c].append((l, r))

segments = []
for team, interval in intervals.items():
    interval.sort()
    for i in range(1, len(interval)):
        l1, r1 = interval[i-1]
        l2, r2 = interval[i]
        segments.append((r1-1, l2, team))

segments.sort()
print(segments)

if len(segments) == 0:
    print(0)
    exit(0)

teamDict = defaultdict(int)
currentTeam = 0
maxTeam = 0
left = 0

for right in range(len(segments)):
    startTime, endTime, team = segments[right]

    teamDict[team] += 1
    if teamDict[team] == 1:
        currentTeam += 1

    while segments[right][1] - segments[left][0] > M:
        leftStartTime, leftEndTime, leftTeam = segments[left]
        teamDict[leftTeam] -= 1
        if teamDict[leftTeam] == 0:
            currentTeam -= 1
        left += 1

    maxTeam = max(maxTeam, currentTeam)

print(maxTeam)