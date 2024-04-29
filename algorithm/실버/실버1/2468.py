import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N = int(input().rstrip())

l = []

def dfs(n, grid, visited, x, y):
    if x >= 0 and y >= 0 and x < n and y < n and not visited[x][y] and grid[x][y] == 1:
        # print(x, y)
        visited[x][y] = True
        dfs(n, grid, visited, x+1, y)
        dfs(n, grid, visited, x-1, y)
        dfs(n, grid, visited, x, y+1)
        dfs(n, grid, visited, x, y-1)
        return True
    else:
        return False


maxNum = 0
ans = 0
for _ in range(N):
    new = list(map(int, input().rstrip().split()))
    maxNum = max(maxNum, max(new))
    l.append(new)

for i in range(0, maxNum + 1):
    grid = [[0 for _ in range(N)] for _ in range(N)]

    for n in range(N):
        for m in range(N):
            if l[n][m] - i > 0:
                grid[n][m] = 1

    # for n in range(N):
        # print(*grid[n])

    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for n in range(N):
        for m in range(N):
            if dfs(N, grid, visited, n, m):
                count += 1

    if count > ans:
        ans = count

print(ans)



