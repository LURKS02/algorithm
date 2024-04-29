def minAttacks(N, scv):
    from functools import lru_cache

    @lru_cache(None)
    def dp(h1, h2, h3):
        if h1 <= 0 and h2 <= 0 and h3 <= 0:
            return 0
        minAttacks = float('inf')
        for dmg1, dmg2, dmg3 in [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]:
            minAttacks = min(minAttacks, 1 + dp(h1 - dmg1, h2 - dmg2, h3 - dmg3))
        return minAttacks

    if N == 1:
        return dp(scv[0], 0, 0)
    elif N == 2:
        return dp(scv[0], scv[1], 0)
    else:
        return dp(scv[0], scv[1], scv[2])

N = int(input())
scv = list(map(int, input().split()))
print(minAttacks(N, scv))