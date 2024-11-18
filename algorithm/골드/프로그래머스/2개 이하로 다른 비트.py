def solution(numbers):
    answer = []

    def toBinary(x):
        ans = ''
        while x > 1:
            n = x % 2
            x = x // 2
            ans = str(n) + ans
        ans = str(x) + ans
        return ans

    def toDecimal(x):
        num = 0
        n = 1
        for i in range(len(x)-1, -1, -1):
            num += n * int(x[i])
            n *= 2
        return num

    for number in numbers:
        binary = toBinary(number)
        zeroPosition = -1

        for i in range(len(binary)):
            if binary[i] == "0":
                zeroPosition = i

        if zeroPosition == -1:
            result = "10" + binary[1:]
            resultNum = toDecimal(result)
            answer.append(resultNum)
        else:
            firstOnePosition = -1
            for i in range(zeroPosition+1, len(binary)):
                if binary[i] == "1":
                    firstOnePosition = i
                    break
            if firstOnePosition != -1:
                binary = binary[:firstOnePosition] + "0" + binary[firstOnePosition+1:]
            binary = binary[:zeroPosition] + "1" + binary[zeroPosition+1:]
            resultNum = toDecimal(binary)
            answer.append(resultNum)

    return answer

print(solution([2, 7]))