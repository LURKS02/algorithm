import sys
input = sys.stdin.readline

N = int(input().rstrip())

grid = []

for _ in range(N):
    l = [c for c in input().rstrip()]
    grid.append(l)

def checkrow(n):
    maxvalue = 1
    linecount = 1
    for i in range(N-1):
        if grid[n][i] == grid[n][i+1]:
            linecount += 1
            if maxvalue < linecount:
                maxvalue = linecount
        else:
            linecount = 1
    return maxvalue

def checkcolumn(n):
    maxvalue = 1
    linecount = 1
    for i in range(N-1):
        if grid[i][n] == grid[i+1][n]:
            linecount += 1
            if maxvalue < linecount:
                maxvalue = linecount
        else:
            linecount = 1
    return maxvalue

maxvalue = 0
for i in range(N):
    for j in range(N-1):
        grid[i][j], grid[i][j+1] = grid[i][j+1], grid[i][j]

        maxvalue = max(maxvalue, checkrow(i), checkcolumn(j), checkcolumn(j+1))

        grid[i][j], grid[i][j + 1] = grid[i][j + 1], grid[i][j]


for j in range(N):
    for i in range(N-1):
        grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]

        maxvalue = max(maxvalue, checkcolumn(j), checkrow(i), checkrow(i+1))

        grid[i][j], grid[i + 1][j] = grid[i + 1][j], grid[i][j]

max1 = 0
for i in range(N):
    linecount = 1
    for j in range(N-1):
        if grid[i][j] == grid[i][j+1]:
            linecount += 1
            if max1 < linecount:
                max1 = linecount
        else:
            linecount = 1

max2 = 0
for i in range(N):
    linecount = 1
    for j in range(N-1):
        if grid[j][i] == grid[j+1][i]:
            linecount += 1
            if max2 < linecount:
                max2 = linecount
        else:
            linecount = 1

print(max(maxvalue, max1, max2))
