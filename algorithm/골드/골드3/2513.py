from collections import deque
import sys
input = sys.stdin.readline

N, K, S = map(int, input().rstrip().split())
leftQ, rightQ = list(), list()

for _ in range(N):
    dist, person = map(int, input().rstrip().split())
    if dist < S:
        leftQ.append((S - dist, person))
    else:
        rightQ.append((dist - S, person))

def service(queue):
    if not queue:
        return 0

    maxDist = 0
    totalDist = 0
    personLimit = K

    while queue:
        dist, person = queue.pop()
        maxDist = max(dist, maxDist)
        if personLimit < person:
            totalDist += maxDist * 2
            queue.append((dist, person - personLimit))
            maxDist = 0
            personLimit = K
        else:
            personLimit -= person

    return totalDist + maxDist * 2

leftQ = deque(sorted(leftQ))
rightQ = deque(sorted(rightQ))

print(service(leftQ) + service(rightQ))

