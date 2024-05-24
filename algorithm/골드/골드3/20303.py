import sys
from collections import deque
input = sys.stdin.readline

# N = 거리에 있는 아이들의 수
# M = 아이들의 친구 관계 수
# K = 울음소리가 공명하기 위한 최소 아이의 수
N, M, K = map(int, input().rstrip().split())

# 아이들이 받은 사탕의 수
candy = list(map(int, input().rstrip().split()))

friends = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    friends[a].append(b)
    friends[b].append(a)

# ========== BFS로 찾기
visited = [False] * (N+1)

def bfs(start):
    deq = deque([start])
    totalCandy = 0
    person = 0

    while deq:
        node = deq.popleft()
        totalCandy += candy[node-1]
        person += 1

        for neighbor in friends[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                deq.append(neighbor)

    return totalCandy, person

candySets = []

for i in range(1, N+1):
    if not visited[i]:
        visited[i] = True
        bfsCandy, bfsPerson = bfs(i)
        candySets.append((bfsCandy, bfsPerson))

# ================ 배낭 문제 해결
dp = [0] * K

for candy, person in candySets:
    for i in range(K-1, person-1, -1):
        dp[i] = max(dp[i], dp[i-person] + candy)

print(dp[K-1])
