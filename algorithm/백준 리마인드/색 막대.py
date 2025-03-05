import sys
from collections import defaultdict

class DisjointSet:
    def __init__(self):
        self.parent = dict()

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x

    def connected_components(self):
        return len(set(self.find(x) for x in self.parent))

degree = defaultdict(int)
dsu = DisjointSet()

while True:
    try:
        line = sys.stdin.readline().strip()

        if not line:
            break

        a, b = line.split()
        degree[a] += 1
        degree[b] += 1

        dsu.add(a)
        dsu.add(b)
        dsu.union(a, b)

    except:
        break

if not degree:
    print("Possible")
    sys.exit()

if dsu.connected_components() > 1:
    print("Impossible")
    sys.exit()

odd_count = sum(1 for x in degree.values() if x % 2 == 1)

if odd_count == 0 or odd_count == 2:
    print("Possible")
else:
    print("Impossible")