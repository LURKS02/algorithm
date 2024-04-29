N = int(input())

l = []

for _ in range(N):
    new = input()
    l.append([int(num) for num in new])

visited = [[False for _ in range(N)] for _ in range(N)]

def dfs(x, y):
    if x >= 0 and y >= 0 and x < N and y < N and not visited[x][y] and l[x][y] == 1:
        visited[x][y] = True
        global count
        count += 1

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

house = []
count = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j] and l[i][j] == 1:
            count = 0
            dfs(i, j)
            house.append(count)


print(len(house))
house.sort()
for num in house:
    print(num)


