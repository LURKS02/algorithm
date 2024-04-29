import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().rstrip().split())
    print(N - 1)