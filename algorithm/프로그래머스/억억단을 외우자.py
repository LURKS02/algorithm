def solution(e, starts):
    divisor=[0 for i in range(e+1)]
    for i in range(2,e+1):
        for j in range(1,min(e//i+1,i)):
            divisor[i*j]+=2
    for i in range(1,int(e**(1/2))+1):
        divisor[i**2]+=1

    divisionMax = [e] * (e+1)
    maxIndex = e
    for i in range(e-1, -1, -1):
        if divisor[i] >= divisor[maxIndex]:
            divisionMax[i] = i
            maxIndex = i
        else:
            divisionMax[i] = maxIndex

    answer = []
    for start in starts:
        answer.append(divisionMax[start])
    # print(answer)
    return answer

solution(8, [1, 3, 7])