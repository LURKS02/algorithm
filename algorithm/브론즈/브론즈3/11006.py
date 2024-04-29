T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    normalcase = M * 2
    print(normalcase - N, M - normalcase + N)
