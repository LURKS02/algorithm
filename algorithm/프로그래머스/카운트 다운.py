target = int(input())

dp = [[float('inf'), -float('inf')]] * 100001
dp[0] = [0, 0]

for i in range(1, 21):
    dp[i] = [1, 1]
    dp[i*2] = [1, 0]
    dp[i*3] = [1, 0]

dp[50] = [1, 1]

if dp[target] != [float('inf'), -float('inf')]:
    print(dp[target])
    exit(0)

for i in range(2, target+1):
    for j in range(1, 61):
        if dp[j][0] + dp[i-j][0] < dp[i][0]:
            dp[i] = [dp[j][0] + dp[i-j][0], dp[j][1] + dp[i-j][1]]
        elif dp[j][0] + dp[i-j][0] == dp[i][0]:
            if dp[j][1] + dp[i-j][1] > dp[i][1]:
                dp[i] = [dp[j][0] + dp[i - j][0], dp[j][1] + dp[i - j][1]]

print(dp[target])