import sys
sys.setrecursionlimit(10**9)

dp = [[[0 for _ in range(0, 21)] for _ in range(0, 21)] for _ in range(0, 21)]

def recursion(a, b, c):

    if a > 0 and b > 0 and c > 0 and a <= 20 and b <= 20 and c <= 20 and dp[a][b][c] != 0:
        return dp[a][b][c]

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return recursion(20, 20, 20)
    elif a < b and b < c:
        dp[a][b][c] = recursion(a, b, c-1) + recursion(a, b-1, c-1) - recursion(a, b-1, c)
    else:
        dp[a][b][c] = recursion(a-1, b, c) + recursion(a-1, b-1, c) + recursion(a-1, b, c-1) - recursion(a-1, b-1, c-1)
    return dp[a][b][c]

while(True):
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print(f'w({a}, {b}, {c}) = {recursion(a, b, c)}')
