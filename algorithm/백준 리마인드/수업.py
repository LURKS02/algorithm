from collections import deque
import bisect
import sys
input = sys.stdin.readline

N = int(input())

students = []

for _ in range(N):
    h, k = map(int, input().split())
    students.append((h, k))

# 키가 큰 순서대로, 랭크가 낮은 순으로
students.sort(key=lambda x: (-x[0], x[1]))

team = deque()

for h, k in students:
    if not team:
        team.append(1)

    else:
        idx = bisect.bisect_left(team, k)
        if idx == len(team):
            team[-1] += 1
        elif idx == 0:
            team.appendleft(1)
        else:
            team[idx-1] += 1

print(len(team))