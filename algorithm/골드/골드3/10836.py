import sys
input = sys.stdin.readline

M, N = map(int, input().rstrip().split())
matrix = [[1] * M for _ in range(M)]

growthMap = [[0] * M for _ in range(M)]
totalGrowth = [0] * (2*M-1)

for _ in range(N):
    growthVal = list(map(int, input().rstrip().split()))
    growthList = [0] * growthVal[0] + [1] * growthVal[1] + [2] * growthVal[2]
    for k in range(2*M-1):
        totalGrowth[k] += growthList[k]

totalIndex = 0
for i in range(M):
    growthMap[M - i - 1][0] = totalGrowth[totalIndex]
    totalIndex += 1
for i in range(1, M):
    growthMap[0][i] = totalGrowth[totalIndex]
    totalIndex += 1

for i in range(1, M):
    for j in range(1, M):
        growthMap[i][j] = growthMap[i-1][j]

for i in range(M):
    for j in range(M):
        matrix[i][j] += growthMap[i][j]


for i in range(M):
    print(*matrix[i])