N = int(input())

l = []
for i in range(N):
    l.append(input())

ans = []

for i in range(len(l[0])):
    if all(l[0][i] == str[i] for str in l):
        ans.append(l[0][i])
        continue
    else:
        ans.append('?')

for c in ans:
    print(c, end='')