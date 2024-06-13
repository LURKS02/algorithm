import sys
from collections import deque
input = sys.stdin.readline

# N = 땅의 크기 (NxN)
# M = 나무의 개수
# K = 지난 년 수
N, M, K = map(int, input().rstrip().split())

energyMap = [[5] * N for _ in range(N)]

# 각 칸에 추가되는 양분의 양
A = []
for _ in range(N):
    A.append(list(map(int, input().rstrip().split())))

# 나무의 정보
trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().rstrip().split())
    trees[x-1][y-1].appendleft(z)

for _ in range(K):
    leaveTrees = []
    dieTrees = []

    for i in range(N):
        for j in range(N):
            deadAmounts = 0
            newTrees = deque()
            while trees[i][j]:
                age = trees[i][j].popleft()
                if energyMap[i][j] >= age:
                    energyMap[i][j] -= age
                    newTrees.append(age+1)
                else:
                    deadAmounts += age // 2
            trees[i][j] = newTrees
            energyMap[i][j] += deadAmounts

    tempTrees = []
    for i in range(N):
        for j in range(N):
            newTrees = deque()
            while trees[i][j]:
                age = trees[i][j].popleft()
                if age % 5 == 0:
                    dx = [0, 0, 1, 1, 1, -1, -1, -1]
                    dy = [1, -1, 0, 1, -1, 0, 1, -1]
                    for k in range(8):
                        nx = i + dx[k]
                        ny = j + dy[k]

                        if 0 <= nx < N and 0 <= ny < N:
                            tempTrees.append((nx, ny))

                newTrees.append(age)
            trees[i][j] = newTrees
            energyMap[i][j] += A[i][j]

    for temp in tempTrees:
        r, c = temp
        trees[r][c].appendleft(1)

    # print(trees)

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += len(trees[i][j])

print(cnt)
