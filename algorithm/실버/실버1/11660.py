import sys
input = sys.stdin.readline

def prefix_sum(matrix):
    n = len(matrix)
    ps = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            ps[i][j] = matrix[i - 1][j - 1] + ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1]

    return ps


def sum_query(ps, x1, y1, x2, y2):
    return ps[x2][y2] - ps[x1 - 1][y2] - ps[x2][y1 - 1] + ps[x1 - 1][y1 - 1]

N, M = map(int, input().rstrip().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().rstrip().split())))

ps_matrix = prefix_sum(matrix)

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    print(sum_query(ps_matrix, x1, y1, x2, y2))