N = int(input())
edges = []
isValid = [[True] * N for _ in range(N)]
ans = 0

for _ in range(N):
    edges.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or j == k or i == k:
                continue

            if edges[i][j] == edges[i][k] + edges[k][j]:
                isValid[i][j] = False

            elif edges[i][j] > edges[i][k] + edges[k][j]:
                ans = -1

if ans != -1:
    for i in range(N):
        for j in range(i, N):
            if isValid[i][j]:
                ans += edges[i][j]

print(ans)
