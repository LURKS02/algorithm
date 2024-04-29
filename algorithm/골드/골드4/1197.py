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
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

V, E = map(int, input().rstrip().split())
edges = []

for _ in range(E):
    A, B, C = map(int, input().rstrip().split())
    edges.append((A-1, B-1, C))

edges.sort(key=lambda x: x[2])

cost = 0
mstEdges = []
unionFind = UnionFind(V)

for u, v, w in edges:
    if unionFind.find(u) != unionFind.find(v):
        unionFind.union(u, v)
        mstEdges.append((u, v, w))
        cost += w
        if len(mstEdges) == V - 1:
            break

if len(mstEdges) == V - 1:
    print(cost)

