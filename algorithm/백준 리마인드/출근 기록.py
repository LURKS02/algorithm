from collections import deque

S = list(input())
L = len(S)
A, B, C = 0, 1, 2

answer = deque()

counts = [0 for _ in range(3)]
for c in S:
    if c == 'A':
        counts[0] += 1
    elif c == 'B':
        counts[1] += 1
    else:
        counts[2] += 1

dp = [[[[[False] * 3 for _ in range(3)] for _ in range(counts[2]+1)] for _ in range(counts[1]+1)] for _ in range(counts[0]+1)]

def dfs(a, b, c, second, first):
    if a == counts[0] and b == counts[1] and c == counts[2]:
        print(''.join(list(answer)))
        exit(0)

    if dp[a][b][c][second][first]:
        return

    dp[a][b][c][second][first] = True

    if a+1 <= counts[0]:
        answer.append('A')
        dfs(a+1, b, c, first, 0)
        answer.pop()

    if b+1 <= counts[1]:
        if first != 1:
            answer.append('B')
            dfs(a, b+1, c, first, 1)
            answer.pop()

    if c+1 <= counts[2]:
        if first != 2 and second != 2:
            answer.append('C')
            dfs(a, b, c+1, first, 2)
            answer.pop()

dfs(0, 0, 0, 0, 0)

print(-1)