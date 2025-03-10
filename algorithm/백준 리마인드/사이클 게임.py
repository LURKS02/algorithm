import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

parents = [i for i in range(n)]
rank = [1 for _ in range(n)]

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False

    if rank[a] < rank[b]:
        parents[a] = b
    else:
        parents[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1

    return True


for i in range(m):
    a, b = map(int, input().split())

    result = union(a, b)
    if not result:
        print(i+1)
        exit(0)

print(0)