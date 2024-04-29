N = int(input())
l = []

il = list(map(int, input().split()))
for i in range(1, N + 1):
    l.insert(il[i - 1], i)

l.reverse()
for x in l:
    print(x, end= ' ')