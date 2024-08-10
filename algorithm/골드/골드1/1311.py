import sys
input = sys.stdin.readline

N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

visited = [-1] * (pow(2, N))

def backtracking(count, visit):
    if count == N:
        return 0

    if visited[visit] != -1:
        return visited[visit]

    ret = 1000000000
    for i in range(N):
        if visit & (1 << i):
            continue
        ret = min(ret, backtracking(count + 1, (visit | (1 << i))) + D[count][i])

    visited[visit] = ret

    return visited[visit]

print(backtracking(0, 0))

