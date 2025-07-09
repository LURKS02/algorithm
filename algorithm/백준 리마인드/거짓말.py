N, M = map(int, input().split())

knowLine = list(map(int, input().split()))
numberOfKnow = knowLine[0]
knowList = knowLine[1:]

parents = [i for i in range(N+1)]

for know in knowList:
    parents[know] = 0

def find(u):
    if parents[u] != u:
        parents[u] = find(parents[u])

    return parents[u]

def union(u, v):
    u = find(u)
    v = find(v)

    if u != v:
        if u < v:
            parents[v] = u
        else:
            parents[u] = v

    return parents[v]

parties = []

for _ in range(M):
    partyLine = list(map(int, input().split()))

    numberOfMember = partyLine[0]
    partyList = partyLine[1:]
    parties.append(partyList)

    for i in range(len(partyList)-1):
        union(partyList[i], partyList[i+1])

canGoSet = set()

for i in range(1, N+1):
    find(i)
    if parents[i] != 0:
        canGoSet.add(i)

answer = 0
for party in parties:
    flag = True
    for i in range(len(party)):
        if party[i] not in canGoSet:
            flag = False
            break

    if flag:
        answer += 1

print(answer)










