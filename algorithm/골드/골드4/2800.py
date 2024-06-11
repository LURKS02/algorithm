from itertools import combinations

inputF = list(input())

gList = []

stack = []
for i in range(len(inputF)):
    char = inputF[i]

    if char == '(':
        stack.append(i)

    elif char == ')':
        idx = stack.pop()
        gList.append((idx, i))

samples = set()
for i in range(1, len(gList) + 1):
    chooseCases = combinations(gList, i)
    for choose in chooseCases:
        chooseSet = set()
        for c in choose:
            chooseSet.add(c[0])
            chooseSet.add(c[1])

        answer = ''
        for j in range(0, len(inputF)):
            if j not in chooseSet:
                answer += inputF[j]

        samples.add(answer)

samples = list(samples)
samples.sort()

for sample in samples:
    print(sample)