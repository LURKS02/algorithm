def lcs_of_three(s1, s2, s3):
    len1, len2, len3 = len(s1), len(s2), len(s3)
    dp = [[[0] * (len3 + 1) for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            for k in range(1, len3 + 1):
                if s1[i-1] == s2[j-1] == s3[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1], dp[i-1][j-1][k], dp[i-1][j][k-1], dp[i][j-1][k-1])

    return dp[len1][len2][len3]

firstString = input()
secondString = input()
thirdString = input()

print(lcs_of_three(firstString, secondString, thirdString))