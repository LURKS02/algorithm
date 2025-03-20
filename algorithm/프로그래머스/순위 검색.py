from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    categoryDict = defaultdict(list)
    answer = []

    languageCategory = ["c", "j", "p"]
    majorCategory = ["b", "f"]
    prosCategory = ["j", "s"]
    foodCategory = ["c", "p"]

    for information in info:
        parsedInformations = list(information.split(" "))
        language = parsedInformations[0]
        major = parsedInformations[1]
        pros = parsedInformations[2]
        food = parsedInformations[3]
        score = int(parsedInformations[4])

        keyword = language[0] + major[0] + pros[0] + food[0]
        categoryDict[keyword].append(score)

    for key in categoryDict:
        categoryDict[key].sort()

    for queryCase in query:
        parsedQueryCase = list(queryCase.split(" "))
        score = parsedQueryCase[-1]
        parsedParameters = list(queryCase.split(" and "))
        parsedParameters[-1] = parsedParameters[-1][:-len(score) - 1]
        score = int(score)
        totalPerson = 0
        totalKeyword = []

        for i in range(len(parsedParameters)):
            parameter = parsedParameters[i]

            if i == 0:
                if parameter == "-":
                    totalKeyword = ["c", "j", "p"]
                else:
                    totalKeyword.append(parameter[0])

            if i == 1:
                tempKeyword = []
                if parameter == "-":
                    for keyword in totalKeyword:
                        tempKeyword.append(keyword + "b")
                        tempKeyword.append(keyword + "f")
                else:
                    for keyword in totalKeyword:
                        tempKeyword.append(keyword + parameter[0])
                totalKeyword = tempKeyword

            if i == 2:
                tempKeyword = []
                if parameter == "-":
                    for keyword in totalKeyword:
                        tempKeyword.append(keyword + "j")
                        tempKeyword.append(keyword + "s")
                else:
                    for keyword in totalKeyword:
                        tempKeyword.append(keyword + parameter[0])
                totalKeyword = tempKeyword

            if i == 3:
                tempKeyword = []
                if parameter == "-":
                    for keyword in totalKeyword:
                        tempKeyword.append(keyword + "c")
                        tempKeyword.append(keyword + "p")
                else:
                    for keyword in totalKeyword:
                        tempKeyword.append(keyword + parameter[0])
                totalKeyword = tempKeyword

        for keyword in totalKeyword:
            index = bisect_left(categoryDict[keyword], score)
            totalPerson += len(categoryDict[keyword]) - index
        answer.append(totalPerson)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
