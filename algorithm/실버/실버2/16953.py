import sys
sys.setrecursionlimit(10**9)

A, B = map(int, input().split())

check = False
def solve(n, count):
    if n > B:
        return -1
    if n == B:
        return count

    r1 = solve(n*2, count + 1)
    r2 = solve(int(f'{n}1'), count + 1)

    if r1 != -1:
        return r1
    return r2

result = solve(A, 1)
print(result)