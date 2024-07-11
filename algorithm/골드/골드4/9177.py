import sys
input = sys.stdin.readline

T = int(input().rstrip())

def canFormWord(first, second, target):
    len1, len2 = len(first), len(second)
    if len1 + len2 != len(target):
        return False

    dp = [[False] * (len2+1) for _ in range(len1+1)]
    dp[0][0] = True

    for i in range(len1+1):
        for j in range(len2+1):
            if i > 0 and dp[i-1][j] and first[i-1] == target[i+j-1]:
                dp[i][j] = True
            if j > 0 and dp[i][j-1] and second[j-1] == target[i+j-1]:
                dp[i][j] = True

    return dp[len1][len2]

for i in range(1, T+1):
    first, second, target = input().split()

    if canFormWord(first, second, target):
        print(f"Data set {i}: yes")
    else:
        print(f"Data set {i}: no")

