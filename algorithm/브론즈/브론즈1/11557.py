T = int(input())

for i in range(T):
    N = int(input())
    max = 0
    ans = ""
    for j in range(N):
        A, B = input().split()
        if max < int(B):
            max = int(B)
            ans = A
    print(ans)