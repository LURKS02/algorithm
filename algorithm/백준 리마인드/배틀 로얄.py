from collections import deque

def solve(n, attack, health):
    alives = deque(range(n))
    keeps = [0] * (n)
    cur = 0
    att = 0

    while len(alives) > 1:
        cur = alives.popleft()
        myHeal = health[cur] - (att - attack[cur] * keeps[cur])
        if myHeal > 0:
            att += attack[cur]
            alives.append(cur)
        keeps[cur] += 1

    return alives[0]

N = int(input())
d = list(map(int, input().split()))
h = list(map(int, input().split()))

print(solve(N, d, h)+1)

