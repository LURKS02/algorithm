from copy import deepcopy

N = int(input())
honeys = list(map(int, input().split()))
copyHoneys = deepcopy(honeys)

answer = 0

for i in range(1, N):
    copyHoneys[i] += copyHoneys[i-1]

# 벌, 벌, 꿀
for i in range(1, N-1):
    answer = max(answer, copyHoneys[N-1] - honeys[0] - honeys[i] + copyHoneys[N-1] - copyHoneys[i])

# 꿀, 벌, 벌
for i in range(1, N-1):
    answer = max(answer, copyHoneys[N-2] - honeys[i] + copyHoneys[i-1])

# 벌, 꿀, 벌
for i in range(1, N-1):
    answer = max(answer, copyHoneys[N-2] - copyHoneys[i-1] + copyHoneys[i] - honeys[0])

print(answer)