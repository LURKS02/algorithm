N = int(input())

l = []

for _ in range(N):
    g = input()
    l.append(g)


l.sort(key=lambda x: (len(x), sum(int(char) for char in x if char.isdigit()), x))
for m in l:
    print(m)