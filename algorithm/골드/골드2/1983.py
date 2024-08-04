N = int(input())

def check(i, r, c):
    maxy = 0
    if 0 <= i - r < len(firstRow) and 0 <= i - c < len(secondRow):
        maxy = dp[r][c] + firstRow[i-r] * secondRow[i-c]
        if 0 < r:
            maxy = max(maxy, dp[r-1][c])
        if 0 < c:
            maxy = max(maxy, dp[r][c-1])
        dp[r][c] = maxy

firstRow = [i for i in map(int, input().split()) if i != 0]
secondRow = [i for i in map(int, input().split()) if i != 0]

firstRowZero = N - len(firstRow)
secondRowZero = N - len(secondRow)

dp = [[0] * (secondRowZero + 1) for _ in range(firstRowZero + 1)]

for i in range(N):
    for r in range(firstRowZero, -1, -1):
        for c in range(secondRowZero, -1, -1):
            check(i, r, c)
print(max(max(row) for row in dp))