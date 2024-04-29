N, M = map(int, input().split())
l = list(map(int, input().split()))

l.sort()

s = []
def getNum():
    if len(s) == M:
        print(" ".join(map(str, s)))

    else:
        for num in l:
            s.append(num)
            getNum()
            s.pop()

getNum()