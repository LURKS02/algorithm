A = input()
B = input()

lenA = len(A)
lenB = len(B)

dp = [[0] * (lenB + 1) for _ in range(lenA + 1)]

for i in range(lenA):
    for j in range(lenB):
        if A[i] == B[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

res = ''
while dp[lenA][lenB] != 0:
    if dp[lenA][lenB] == dp[lenA-1][lenB]:
        lenA -= 1
    elif dp[lenA][lenB] == dp[lenA][lenB-1]:
        lenB -= 1
    else:
        res += A[lenA-1]
        lenA -= 1
        lenB -= 1

print(res[::-1])