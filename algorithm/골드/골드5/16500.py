import sys
input = sys.stdin.readline
S = list(input().rstrip())
N = int(input())

dp = [False] * (len(S) + 1)
dp[0] = True

words = [list(input().rstrip()) for _ in range(N)]

for i in range(len(S)+1):
    for word in words:
        wordLen = len(word)
        if i >= wordLen and dp[i-wordLen] and S[i-wordLen:i] == list(word):
            dp[i] = True

if dp[len(S)]:
    print(1)
else:
    print(0)