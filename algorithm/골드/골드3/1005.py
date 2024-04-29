import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

T = int(input().rstrip())

def graphSearch(dict, goal, times, dp):
    if dp[goal] != -1:
        return dp[goal]

    else:
        goalValue = 0
        for d in dict[goal]:
            goalValue = max(goalValue, graphSearch(dict, d, times, dp))
        dp[goal] = goalValue + times[goal-1]
        return dp[goal]

for _ in range(T):
    N, K = map(int, input().rstrip().split())
    buildingTime = list(map(int, input().rstrip().split()))
    buildingRule = {}
    for _ in range(K):
        fromB, toB = map(int, input().rstrip().split())
        if toB in buildingRule:
            buildingRule[toB].append(fromB)
        else:
            buildingRule[toB] = [fromB]

    W = int(input().rstrip())

    dp = [-1 for _ in range(N + 1)]
    for i in range(1, N + 1):
        if i not in buildingRule:
            dp[i] = buildingTime[i-1]

    # print(dp)

    print(graphSearch(buildingRule, W, buildingTime, dp))
    # print(dp)



