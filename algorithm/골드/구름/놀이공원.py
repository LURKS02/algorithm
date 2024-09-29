T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    minValue = float('inf')

    for i in range(0, N-K+1):
        for j in range(0, N-K+1):
            value = 0
            for m in range(i, i+K):
                for n in range(j, j+K):
                    value += info[m][n]
            minValue = min(minValue, value)

    print(minValue)