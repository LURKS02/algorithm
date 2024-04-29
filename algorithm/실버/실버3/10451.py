import sys
sys.setrecursionlimit(2000)

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        parent[rootY] = rootX

def count_cycles(perm):
    n = len(perm) - 1
    parent = [i for i in range(0, n + 1)]

    for i in range(1, n+1):
        union(parent, i, perm[i])

    return sum(parent[i] == i for i in range(1, n+1))

T = int(input())
for _ in range(T):
    n = int(input())
    perm = [0]
    l = list(map(int, input().split()))
    perm = perm + l
    print(count_cycles(perm))