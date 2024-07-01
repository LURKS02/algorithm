from collections import deque, defaultdict

N, M = map(int, input().split())
king = input().rstrip()

family = {}
children = defaultdict(list)
degree = defaultdict(int)

for _ in range(N):
    child, parent1, parent2 = input().rstrip().split()
    family[child] = (parent1, parent2)
    children[parent1].append(child)
    children[parent2].append(child)

    degree[child] += 2
    degree[parent1] += 0
    degree[parent2] += 0

claimants = [input().strip() for _ in range(M)]

bloodline = defaultdict(float)
bloodline[king] = 1.0

deq = deque()

for k in degree.keys():
    if degree[k] == 0:
        deq.append(k)

while deq:
    person = deq.popleft()
    for child in children[person]:
        bloodline[child] += bloodline[person] / 2
        # print(bloodline)
        degree[child] -= 1
        # print(degree[child])
        if degree[child] == 0:
            deq.append(child)

maxBloodline = -1
heir = None

# print(bloodline)

for claimant in claimants:
    if bloodline[claimant] > maxBloodline:
        maxBloodline = bloodline[claimant]
        heir = claimant

print(heir)