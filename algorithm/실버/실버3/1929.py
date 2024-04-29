def che(M, N):
    l = [True for _ in range(N+1)]
    start = 2
    while(start * start <= N):
        if l[start]:
            for i in range(start*start, N + 1, start):
                l[i] = False
        start += 1

    ans = []
    for i in range(M, N+1):
        if i != 0 and i != 1 and l[i]:
            ans.append(i)
    return ans


M, N = map(int, input().split())
new = che(M, N)
for num in new:
    print(num)