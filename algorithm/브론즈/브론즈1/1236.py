N, M = map(int, input().split())

l = []

for i in range(N):
    l.append(input())

vc = 0
hc = 0

for i in range(M):
    con = False
    for j in range(N):
        if l[j][i] == 'X':
            con = True
    if con == False:
        hc += 1

for i in range(N):
    con = False
    if 'X' in l[i]:
        con = True
    if con == False:
        vc += 1

print(max(vc, hc))