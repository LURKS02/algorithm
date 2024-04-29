import sys
sys.setrecursionlimit(10**9)

N, r, c = map(int, input().split())

def find_position(N, r, c):
    if N == 0:
        return 0
    half = 2 ** (N - 1)

    if r < half and c < half:
        return find_position(N - 1, r, c)
    elif r < half and c >= half:
        return half * half + find_position(N - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + find_position(N - 1, r - half, c)
    else:
        return 3 * half * half + find_position(N - 1, r - half, c - half)

print(find_position(N, r, c))
