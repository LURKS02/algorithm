N, R, B, G = map(int, input().split())

dp = [[[[0] * (G+1) for _ in range(B+1)] for _ in range(R+1)] for _ in range(N+1)]

dp[0][R][B][G] = 1

def comb(N, r):
    if r == N or r == 0:
        return 1
    return comb(N-1, r-1) + comb(N-1, r)

for i in range(0, N):
    for a in range(R+1):
        for b in range(B+1):
            for c in range(G+1):
                if not dp[i][a][b][c]:
                    continue
                if (i+1) % 3 == 0:
                    temp = (i+1) // 3
                    if a >= temp and b >= temp and c >= temp:
                        dp[i+1][a-temp][b-temp][c-temp] += dp[i][a][b][c] * comb(temp*3, temp) * comb(temp*2, temp)
                if (i+1) % 2 == 0:
                    temp = (i+1) // 2
                    if a >= temp and b >= temp:
                        dp[i+1][a-temp][b-temp][c] += dp[i][a][b][c] * comb(temp * 2, temp)
                    if a >= temp and c >= temp:
                        dp[i+1][a-temp][b][c-temp] += dp[i][a][b][c] * comb(temp * 2, temp)
                    if b >= temp and c >= temp:
                        dp[i+1][a][b-temp][c-temp] += dp[i][a][b][c] * comb(temp * 2, temp)

                if a >= i+1:
                    dp[i+1][a-i-1][b][c] += dp[i][a][b][c]
                if b >= i+1:
                    dp[i+1][a][b-i-1][c] += dp[i][a][b][c]
                if c >= i+1:
                    dp[i+1][a][b][c-i-1] += dp[i][a][b][c]

answer = 0
for a in range(R+1):
    for b in range(B+1):
        for c in range(G+1):
            answer += dp[N][a][b][c]

print(answer)