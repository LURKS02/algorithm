first_string = input()
second_string = input()

N, M = len(first_string), len(second_string)

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if first_string[i-1] == second_string[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

lcs_length = dp[N][M]

lcs = ''
i, j = N, M

while i > 0 and j > 0:
    if first_string[i-1] == second_string[j-1]:
        lcs = first_string[i-1] + lcs
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

print(lcs_length)
print(lcs)