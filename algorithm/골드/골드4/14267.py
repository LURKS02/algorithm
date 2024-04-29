import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
superiors = list(map(int, input().rstrip().split()))
subordinates = [[] for _ in range(N)]

for i in range(1, N):
    superior = superiors[i] - 1
    subordinates[superior].append(i)

praise = [0] * N

for _ in range(M):
    i, w = map(int, input().rstrip().split())
    praise[i-1] += w

def dfs(employee):
    for subordinate in subordinates[employee]:
        praise[subordinate] += praise[employee]
        dfs(subordinate)

dfs(0)
print(' '.join(map(str, praise)))