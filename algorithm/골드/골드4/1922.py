import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_v] > self.rank[root_u]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

N = int(input().rstrip())
M = int(input().rstrip())

line = []

for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    line.append((a-1, b-1, c))

line.sort(key=lambda x: x[2])

cost = 0
costLines = []
unionFind = UnionFind(N)

for u, v, w in line:
    if unionFind.find(u) != unionFind.find(v):
        unionFind.union(u, v)
        costLines.append((u, v, w))
        cost += w
        if len(costLines) == N-1:
            break

print(cost)