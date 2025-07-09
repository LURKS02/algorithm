import sys
import bisect
from collections import defaultdict

input = sys.stdin.readline

N, Q = map(int, input().split())

d = defaultdict(list)

for _ in range(N):
    time, level = input().split("#")

    for l in range(1, int(level)+1):
        d[l].append(time)

results = []

for _ in range(Q):
    startTime, endTime, level = input().split("#")
    answer = 0

    li = bisect.bisect_left(d[int(level)], startTime)
    ri = bisect.bisect_right(d[int(level)], endTime)

    answer += ri - li

    results.append(answer)

print("\n".join(map(str, results)))