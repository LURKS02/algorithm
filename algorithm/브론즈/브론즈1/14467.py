N = int(input())

cows = [-1] * 10
count = 0

for i in range(N):
    N, D = map(int, input().split())
    if cows[N - 1] == -1:
        cows[N - 1] = D
    else:
        if cows[N - 1] != D:
            cows[N - 1] = D
            count += 1

print(count)