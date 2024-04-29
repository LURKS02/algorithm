import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

dict = {}

for _ in range(M):
    A, B = map(int, input().rstrip().split())

    if A in dict and B not in dict[A]:
        dict[A].append(B)
    else:
        dict[A] = [B]

    if B in dict and A not in dict[B]:
        dict[B].append(A)
    else:
        dict[B] = [A]

def bfs(A, B):

    deq = deque()
    deq.append((A, 0))

    visited = [False for _ in range(N)]
    visited[A-1] = True

    while(deq):
        node, count = deq.popleft()
        if node == B:
            return count
        for n in dict[node]:
            if not visited[n-1]:
                visited[n-1] = True
                deq.append((n, count + 1))

    return -1

nums = []

for node in range(1, N+1):
    count = 0
    for dir in range(1, N+1):
        if node == dir:
            continue
        else:
            count += bfs(node, dir)
    nums.append(count)

min = 1e9
person = -1

for i in range(len(nums)):
    if nums[i] < min:
        min = nums[i]
        person = i + 1

#print(nums)
print(person)
