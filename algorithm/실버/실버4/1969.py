N, M = map(int, input().split())

l = []
for _ in range(N):
    l.append(input())

newl = []
for i in range(M):
    n = []
    for j in range(N):
        n.append(l[j][i])
    newl.append(n)

count = 0
ans = []
for s in newl:
    A = s.count('A')
    T = s.count('T')
    G = s.count('G')
    C = s.count('C')
    if max(A, T, G, C) == A:
        ans.append('A')
    elif max(A, T, G, C) == C:
        ans.append('C')
    elif max(A, T, G, C) == G:
        ans.append('G')
    elif max(A, T, G, C) == T:
        ans.append('T')
    count += N - max(A,T,G,C)

for c in ans:
    print(c, end='')
print()
print(count)
