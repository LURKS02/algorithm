def solution(skill, skill_trees):
    answer = 0

    for skillTree in skill_trees:
        idx = 0
        skillCount = 0
        for st in skillTree:
            if idx < len(skill) and skill[idx] == st:
                skillCount += 1
                idx += 1

        skillSet = set(skill)
        skCount = 0
        for st in skillTree:
            if st in skillSet:
                skCount += 1

        if skillCount == skCount:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))