def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    rootX = find(x, parent)
    rootY = find(y, parent)

    if rootX != rootY:
        parent[rootX] = rootY

G = int(input())
P = int(input())

parent = [i for i in range(G + 1)]
count = 0

for _ in range(P):
    gi = int(input())
    docking_gate = find(gi, parent)
    if docking_gate == 0:
        break
    union(docking_gate, docking_gate-1, parent)
    count += 1

print(count)