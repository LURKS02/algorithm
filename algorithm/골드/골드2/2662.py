N, M = map(int, input().split())

company = [[] for _ in range(M)]

for _ in range(N):
    l = list(map(int, input().split()))
    for i in range(0, len(l)-1):
        company[i].append(l[i+1])
# print(company)

# dp = [총 투자금][고려한 회사의 수]
dp = [[0] * (M+1) for _ in range(N+1)]
investment = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, M+1): # M까지의 기업 고려
    for j in range(1, N+1): # 1~N까지의 투자금에 대해
        for k in range(j + 1): #0부터 j까지 투자 가능 금액
            currentProfit = company[i-1][k-1] if k > 0 else 0

            if dp[j][i] < dp[j-k][i-1] + currentProfit:
                dp[j][i] = dp[j-k][i-1] + currentProfit
                investment[j][i] = k

maxProfit = dp[N][M]
invested = [0] * M
remaining = N

for i in range(M, 0, -1):
    invested[i-1] = investment[remaining][i]
    remaining -= invested[i-1]

print(maxProfit)
print(' '.join(map(str, invested)))