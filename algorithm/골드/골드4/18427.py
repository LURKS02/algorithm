import sys
input = sys.stdin.readline

# N = 학생의 수
# M = 한 학생이 가질 수 있는 최대 블록 수
# H = 만들고자 하는 높이
N, M, H = map(int, input().rstrip().split())

# 학생들이 가지고 있는 블록 정보
students = []
for _ in range(N):
    students.append(list(map(int, input().rstrip().split())))

def solveBlocks():
    MOD = 10007

    # dp = [경우의 수] * 높이
    dp = [0] * (H+1)
    dp[0] = 1

    # 각 학생의 블록을 고려
    for blocks in students:
        for j in range(H, 0, -1):
            for block in blocks:
                if j >= block:
                    dp[j] = (dp[j] + dp[j - block]) % MOD

    return dp[H]

print(solveBlocks())