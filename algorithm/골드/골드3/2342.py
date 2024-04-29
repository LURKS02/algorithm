def move_cost(from_pos, to_pos):
    if from_pos == to_pos:
        return 1
    if from_pos == 0 or to_pos == 0:
        return 2
    if abs(from_pos - to_pos) == 2:
        return 4
    return 3

def min_energy(steps):
    dp = [[[float('inf') for _ in range(5)] for _ in range(5)] for _ in range(len(steps) + 1)]
    dp[0][0][0] = 0

    for i in range(1, len(steps) + 1):
        step = steps[i-1]

        for left in range(5):
            for right in range(5):
                # 오른발이 움직이는 경우
                if left != step:
                    dp[i][left][step] = min(dp[i][left][step], dp[i-1][left][right] + move_cost(right, step))

                if right != step:
                    dp[i][step][right] = min(dp[i][step][right], dp[i-1][left][right] + move_cost(left, step))

    final_energy = float('inf')
    for left in range(5):
        for right in range(5):
            final_energy = min(final_energy, dp[len(steps)][left][right])

    return final_energy


steps = list(map(int, input().split()))

print(min_energy(steps[:-1]))