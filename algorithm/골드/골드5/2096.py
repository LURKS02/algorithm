# import sys
#
# N = int(input().rstrip())
#
# matrix = []
#
# for _ in range(N):
#     matrix.append(list(map(int, input().rstrip().split())))
#
# dp = [[[0, 0] for _ in range(3)] for _ in range(N)]
#
# for i in range(N):
#     for j in range(3):
#         if i == 0:
#             for j in range(3):
#                 dp[i][j][0] = matrix[i][j]
#                 dp[i][j][1] = matrix[i][j]
#
#         else:
#             dp[i][0][0] = min(dp[i-1][0][0], dp[i-1][1][0]) + matrix[i][0]
#             dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][1]) + matrix[i][0]
#
#             dp[i][1][0] = min(dp[i-1][0][0], dp[i-1][1][0], dp[i-1][2][0]) + matrix[i][1]
#             dp[i][1][1] = max(dp[i-1][0][1], dp[i-1][1][1], dp[i-1][2][1]) + matrix[i][1]
#
#             dp[i][2][0] = min(dp[i-1][1][0], dp[i-1][2][0]) + matrix[i][2]
#             dp[i][2][1] = max(dp[i-1][1][1], dp[i-1][2][1]) + matrix[i][2]
#
# print(max(dp[N-1][0][1], dp[N-1][1][1], dp[N-1][2][1]), min(dp[N-1][0][0], dp[N-1][1][0], dp[N-1][2][0]))

N = int(input())

max_dp = [[0] * 3 for _ in range(2)]
min_dp = [[0] * 3 for _ in range(2)]

first_line = list(map(int, input().split()))
for i in range(3):
    max_dp[0][i] = min_dp[0][i] = first_line[i]

for _ in range(1, N):
    line = list(map(int, input().split()))
    for i in range(3):
        max_dp[1][i] = max(max_dp[0][max(0, i-1):min(3, i+2)]) + line[i]
        min_dp[1][i] = min(min_dp[0][max(0, i-1):min(3, i+2)]) + line[i]

    max_dp[0], max_dp[1] = max_dp[1], max_dp[0]
    min_dp[0], min_dp[1] = min_dp[1], min_dp[0]

# print(max_dp)
# print(min_dp)

print(max(max_dp[0]), min(min_dp[0]))