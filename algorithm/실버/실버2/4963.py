import sys
sys.setrecursionlimit(10**7)

def dfs(visited, i, j, w, h):
    if i >= h or i < 0 or j >= w or j < 0 or visited[i][j] or l[i][j] == 0:
        return
    else:
        visited[i][j] = True

        dfs(visited, i + 1, j, w, h)
        dfs(visited, i, j + 1, w, h)
        dfs(visited, i - 1, j, w, h)
        dfs(visited, i, j - 1, w, h)
        dfs(visited, i + 1, j + 1, w, h)
        dfs(visited, i + 1, j - 1, w, h)
        dfs(visited, i - 1, j + 1, w, h)
        dfs(visited, i - 1, j - 1, w, h)


while(True):
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    else:
        l = []
        for _ in range(h):
            newl = list(map(int, input().split()))
            l.append(newl)

        visited = [[False for _ in range(w)] for _ in range(h)]

        count = 0
        for i in range(h):
            for j in range(w):
                if l[i][j] == 1 and visited[i][j] == False:
                    dfs(visited, i, j, w, h)
                    count += 1

        print(count)