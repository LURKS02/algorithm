N = int(input())
grades = [0]

dp = []
for _ in range(N):
    grades.append(int(input()))

dp.append(0)
if len(grades) >= 2:
    dp.append(grades[1])
if len(grades) >= 3:
    dp.append(grades[1] + grades[2])

for i in range(3, N + 1):
    dp.append(grades[i] + max(dp[i - 3] + grades[i - 1], dp[i - 2]))

print(dp[N])