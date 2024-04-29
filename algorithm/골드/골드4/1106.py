C, N = map(int, input().split())
c = []
p = []

for _ in range(N):
    cost, people = map(int, input().split())
    c.append(cost)
    p.append(people)

maxPeople = max(p)

dp = [float('inf') for _ in range(C + maxPeople)]

for i in range(N):
    dp[p[i]] = c[i]
dp[0] = 0

for i in range(C + maxPeople):
    for j in range(N):
        idx = i - p[j]
        if idx >= 0:
            dp[i] = min(dp[i], dp[idx] + c[j])

# print(dp)

# print(dp)
print(min(dp[C: C + maxPeople]))
