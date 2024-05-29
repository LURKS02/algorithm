import sys
input = sys.stdin.readline

# N = 도시의 개수 (300)
# M = 최대 이동 도시 개수 (300)
# K = 항공로 정보의 개수 (100,000)
N, M, K = map(int, input().rstrip().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(K):
    # a -> b 기내식의 점수 c
    a, b, c = map(int, input().rstrip().split())
    if a > b:
        continue
    graph[a][b] = max(graph[a][b], c)

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(2, N+1):
    dp[i][2] = graph[1][i]

for i in range(2, N+1):
    for j in range(3, M+1):
        for l in range(1, i):
            if graph[l][i] and dp[l][j-1]:
                dp[i][j] = max(dp[i][j], dp[l][j-1] + graph[l][i])

print(max(dp[N]))

