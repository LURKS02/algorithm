T = int(input())

for _ in range(T):
    N = int(input())
    numArr = list(map(int, list(input())))
    charArr = list(input())

    result = 0

    dir = [-1, 0, 1]

    for i in range(N):
        if i == 0:
            if numArr[0] != 0 and numArr[1] != 0:
                numArr[0] -= 1
                numArr[1] -= 1
                result += 1
        elif i == N-1:
            if numArr[i] != 0 and numArr[i-1] != 0:
                numArr[i] -= 1
                numArr[i-1] -= 1
                result += 1

        else:
            if numArr[i-1] != 0 and numArr[i] != 0 and numArr[i+1] != 0:
                numArr[i-1] -= 1
                numArr[i] -= 1
                numArr[i+1] -= 1
                result += 1

    print(result)