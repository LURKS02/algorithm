def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        answer.append(getAnswer(i))
    return answer

def getAnswer(n):
    if n == 1:
        return 0
    else:
        p = 2
        maxValue = -1
        while p * p <= n:
            if n % p == 0:
                if p <= 10000000:
                    maxValue = max(maxValue, p)
                if n // p <= 10000000:
                    maxValue = max(maxValue, n//p)
            p += 1

        return max(maxValue, 1)

print(solution(100000014, 100000016))