import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

dict = {}

visited = [False for _ in range(n+1)]

for _ in range(m):
    A, B = map(int, input().rstrip().split())
    if A in dict:
        dict[A].append(B)
    else:
        dict[A] = [B]
    if B in dict:
        dict[B].append(A)
    else:
        dict[B] = [A]

d = deque()

d.append((1, 0))

while(d):
    check = d.popleft()
    if not visited[check[0]]:
        visited[check[0]] = True
    if check[0] in dict and check[1] <= 1:
        for n in dict[check[0]]:
            d.append((n, check[1] + 1))


count = 0

for k in visited:
    if k:
        count += 1

print(count - 1)