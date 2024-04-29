A, B, C = map(int, input().split())

if C - B <= 0:
    print(-1)

else:
    t = C - B
    print(A // t + 1)