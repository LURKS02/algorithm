elements = list(map(int, input().split()))

tempElements = elements + elements
ps = [0]
for i in range(len(tempElements)):
    ps.append(ps[-1] + tempElements[i])

sumSet = set()
for i in range(1, len(elements)+1):
    for j in range(0, len(elements)):
        sumSet.add(ps[j+i]-ps[j])
print(len(sumSet))