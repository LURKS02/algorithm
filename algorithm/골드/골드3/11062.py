def optimal_score(cards):
    n = len(cards)
    # 총합을 미리 계산
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + cards[i]

    # dp 배열 초기화
    dp = [[0] * n for _ in range(n)]

    # 길이가 1인 구간 초기화
    for i in range(n):
        dp[i][i] = cards[i]

    # 구간의 길이를 늘려가며 계산
    for length in range(2, n + 1):  # 길이 2부터 n까지
        for start in range(n - length + 1):
            end = start + length - 1
            # 현재 구간의 총합
            total_sum = prefix_sum[end + 1] - prefix_sum[start]
            # 왼쪽 카드를 선택하거나 오른쪽 카드를 선택했을 때
            left_choice = cards[start] + (total_sum - cards[start] - dp[start + 1][end])
            right_choice = cards[end] + (total_sum - cards[end] - dp[start][end - 1])
            dp[start][end] = max(left_choice, right_choice)

    return dp[0][n - 1]


# 입력 받기 및 출력 처리
import sys

T = int(input())
results = []
for _ in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    results.append(optimal_score(cards))

for result in results:
    print(result)