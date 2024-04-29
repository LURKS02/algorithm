N = int(input())
l = []

for i in range(N):
    l.append(list(map(int, input().split())))

t = [0] * N

for i in range(len(l)):
    for j in range(len(l)):
        for k in range(5):
            if l[i][k] == l[j][k]:
                t[i] += 1
                break

m = max(t)
print(t.index(m) + 1)
