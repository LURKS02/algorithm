import sys
sys.setrecursionlimit(10**9)

N = int(input())
visited = [False] * N

mp, mf, ms, mv = map(int, input().split())

foods = []

for _ in range(N):
    p, f, s, v, c = map(int, input().split())
    foods.append((p, f, s, v, c))

ans = float('inf')
ansset = set()

def dfs(idx, A, B, C, D, cost):
    global ans
    global ansset
    if A >= mp and B >= mf and C >= ms and D >= mv:
        if cost < ans:
            ans = cost
            ansset = set([i+1 for i in range(N) if visited[i] == True])

    if idx == N-1:
        return

    fp, ff, fs, fv, fc = foods[idx+1]
    np, nf, ns, nv, nc = A + fp, B + ff, C + fs, D + fv, cost + fc
    visited[idx+1] = True
    dfs(idx+1, np, nf, ns, nv, nc)
    visited[idx+1] = False
    dfs(idx+1, A, B, C, D, cost)

dfs(-1, 0, 0, 0,0, 0)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
    print(*sorted(list(ansset)))
