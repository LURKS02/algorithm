from math import sqrt

N = int(input())

stars = []

for i in range(N):
    x, y = map(float, input().split())
    stars.append((x, y))

distances = []

for i in range(len(stars)):
    for j in range(i+1, len(stars)):
        dist = sqrt(pow(stars[i][0] - stars[j][0], 2) + pow(stars[i][1] - stars[j][1], 2))
        distances.append((i, j, dist))

distances.sort(key=lambda x: x[2])

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

cost = 0
costLines = []
unionFind = UnionFind(N)

for u, v, w in distances:
    if unionFind.find(u) != unionFind.find(v):
        unionFind.union(u, v)
        costLines.append((u, v, w))
        cost += w
        if len(costLines) == N-1:
            break

print(round(cost, 2))