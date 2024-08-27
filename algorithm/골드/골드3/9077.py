import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    dict = {}
    maxMines = 0

    N = int(input())

    for _ in range(N):
        x, y = map(int, input().split())

        for i in range(-5, 5 + 1):
            for j in range(-5, 5 + 1):
                key = (x + i) * 20000 + (y + j)
                dict[key] = dict.get(key, 0) + 1
                maxMines = max(maxMines, dict[key])

    print(maxMines)