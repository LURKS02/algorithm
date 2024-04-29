from itertools import combinations

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def maxEnemiesElimated(N, M, D, board):
    max_count = 0

    for archers in combinations(range(M), 3):
        count = simulate(N, M, D, board, archers)
        max_count = max(max_count, count)

    return max_count

def simulate(N, M, D, board, archers):
    count = 0
    enemies = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 1]

    while enemies:
        to_attack = []

        for archer in archers:
            archer_row, archer_col = N, archer
            min_distance = float('inf')
            target = None

            for (r, c) in enemies:
                distance = abs(archer_row - r) + abs(archer_col - c)
                if distance <= D:
                    if distance < min_distance or (distance == min_distance and c < target[1]):
                        min_distance = distance
                        target = (r, c)
            if target:
                to_attack.append(target)

        to_attack = set(to_attack)
        count += len(to_attack)
        enemies = [(r, c) for (r, c) in enemies if (r, c) not in to_attack]

        enemies = [(r+1, c) for (r, c) in enemies if r+1 < N]

    return count

print(maxEnemiesElimated(N, M, D, board))