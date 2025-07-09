
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = dict()

def dfs(node, visited):
    if visited == (1 << N) - 1:
        if matrix[node][0]:
            return matrix[node][0]
        else:
            return float('inf')

    if (node, visited) in dp:
        return dp[(node, visited)]

    minCost = float('inf')
    for neighbor in range(1, N):
        if matrix[node][neighbor] == 0 or visited & (1 << neighbor):
            continue
        cost = dfs(neighbor, visited | (1 << neighbor)) + matrix[node][neighbor]
        minCost = min(cost, minCost)

    dp[(node, visited)] = minCost

    return minCost

print(dfs(0, 1))
