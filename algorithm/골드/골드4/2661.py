N = int(input())
result = []

def check(result, cnt):
    for i in range(cnt):
        sliceTemp = result[i:]
        for j in range(1, len(sliceTemp)//2+1):
            if sliceTemp[:j] == sliceTemp[j:j+j]:
                return False

    return True

def Backtracking(cnt):
    if not check(result, cnt):
        return -1

    if cnt == N:
        print(*result, sep='')
        return 1

    for i in range(1, 4):
        result.append(i)
        if Backtracking(cnt+1) == 1:
            return 1
        result.pop()

Backtracking(0)