N = int(input())
arr = [(0, 0, 0, 0)]
# 번호, 넓이, 높이, 무게

for i in range(N):
    s, h, w = map(int, input().split())
    arr.append((i+1, s, h, w))

arr.sort(key=lambda x: x[3])

dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + arr[i][2])

result = []
maxH = max(dp)
idx = dp.index(maxH)

while True:
    if maxH == dp[idx]:
        result.append(arr[idx][0])
        maxH -= arr[idx][2]
    idx -= 1
    if idx == 0:
        break

print(len(result))
for i in range(len(result) - 1, -1, -1):
    print(result[i])