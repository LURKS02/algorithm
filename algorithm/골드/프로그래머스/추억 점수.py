def solution(name, yearning, photo):
    answer = []
    nameSet = set(name)
    yearningDict = {}

    for i in range(len(name)):
        yearningDict[name[i]] = yearning[i]

    for p in photo:
        sum = 0
        for ph in p:
            if ph in nameSet:
                sum += yearningDict[ph]
        answer.append(sum)

    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))