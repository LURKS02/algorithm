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

N, M = map(int, input().rstrip().split())
lines = []

for _ in range(M):
    A, B, C = map(int,input().rstrip().split())
    lines.append((A-1, B-1, C))

lines.sort(key=lambda x: x[2])
unionFind = UnionFind(N)

cost = 0
maxCost = 0
edges = []

for u, v, w in lines:
    if unionFind.find(u) != unionFind.find(v):
        unionFind.union(u, v)
        edges.append((u, v, w))
        cost += w
        if maxCost < w:
            maxCost = w
        if len(edges) == N-1:
            break

print(cost - maxCost)