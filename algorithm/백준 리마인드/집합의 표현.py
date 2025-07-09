n, m = map(int, input().split())

parents = [i for i in range(n+1)]

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[b] = a

for _ in range(m):
    line = list(map(int, input().split()))

    if line[0] == 0:
        union(line[1], line[2])
    else:
        if find(line[1]) == find(line[2]):
            print("YES")
        else:
            print("NO")