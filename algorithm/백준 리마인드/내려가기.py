import sys
input = sys.stdin.readline

N = int(input())

maxDP = [[0 for _ in range(3)] for _ in range(2)]
minDP = [[float('inf') for _ in range(3)] for _ in range(2)]
minDP[0] = [0, 0, 0]

idx = 1
for _ in range(N):
    line = list(map(int, input().split()))

    for i in range(3):
        # 맨 왼쪽
        if i == 0:
            maxDP[idx][0] = max(maxDP[idx-1][0], maxDP[idx-1][1]) + line[0]
            minDP[idx][0] = min(minDP[idx - 1][0], minDP[idx - 1][1]) + line[0]

        # 맨 오른쪽
        elif i == 2:
            maxDP[idx][2] = max(maxDP[idx-1][1], maxDP[idx-1][2]) + line[-1]
            minDP[idx][2] = min(minDP[idx - 1][1], minDP[idx - 1][2]) + line[-1]

        else:
            maxDP[idx][i] = max(maxDP[idx-1][i-1], maxDP[idx-1][i], maxDP[idx-1][i+1]) + line[i]
            minDP[idx][i] = min(minDP[idx - 1][i - 1], minDP[idx - 1][i], minDP[idx - 1][i + 1]) + line[i]

    if idx == 1:
        idx = 0
    else:
        idx = 1

if idx == 1:
    idx = 0
else:
    idx = 1

print(max(maxDP[idx]), min(minDP[idx]))