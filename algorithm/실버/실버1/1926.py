import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

picture = []

visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    picture.append(list(map(int, input().rstrip().split())))

def dfs(picture, visited, x, y):
    if x >= 0 and y >= 0 and x < n and y < m and picture[x][y] == 1 and not visited[x][y]:
        global count
        count += 1
        visited[x][y] = True

        dfs(picture, visited, x+1, y)
        dfs(picture, visited, x-1, y)
        dfs(picture, visited, x, y+1)
        dfs(picture, visited, x, y-1)

        return True

    else:
        return False

countarray = []

picturecount = 0

for i in range(n):
    for j in range(m):
        count = 0
        if dfs(picture, visited, i, j):
            picturecount += 1
            countarray.append(count)

print(picturecount)
if countarray:
    print(max(countarray))
else:
    print(0)