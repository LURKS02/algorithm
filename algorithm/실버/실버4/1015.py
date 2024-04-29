N = int(input())

anslist = [0] * N

A = list(map(int, input().split()))

s = set(A)
count = 0
while(len(s) > 0):
    minnum = min(s)
    for i in range(N):
        if A[i] == minnum:
            anslist[i] = count
            count += 1
    s.remove(minnum)
for n in anslist:
    print(n, end=' ')