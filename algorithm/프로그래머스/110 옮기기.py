
def solution(s):
    answer = []

    for str in s:
        l = list(str)
        stack = []
        number110 = 0

        for c in l:
            if c == "0" and len(stack) >= 2:
                if stack[-1] == "1" and stack[-2] == "1":
                    stack.pop()
                    stack.pop()
                    number110 += 1
                else:
                    stack.append(c)
            else:
                stack.append(c)

        broken = False
        for i in range(len(stack)-1, -1, -1):
            if stack[i] == "0":
                ansString = "".join(stack[:i+1]) + "110" * number110 + "".join(stack[i+1:])
                answer.append(ansString)
                broken = True
                break

        if not broken:
            ansString = "110" * number110 + "".join(stack)
            answer.append(ansString)

    return answer

print(solution(["1110","100111100","0111111010"]))