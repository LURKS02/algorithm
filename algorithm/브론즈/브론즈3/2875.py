N, M, K = map(int, input().split())

n = N // 2
m = M

team = min(n, m)

N -= team*2
M -= team

total = N + M

if total >= K:
    print(team)
else:
    any = abs(total - K)
    if any % 3 == 0:
        k = any // 3
    else:
        k = any // 3 + 1
    print(team - k)