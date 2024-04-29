A, P = map(int, input().split())
s = set()
s.add(A)
l = []
l.append(A)

while(True):
    breakpoint=False
    A = str(A)
    count = 2
    sum = 0
    for c in A:
        sum += pow(int(c), P)
    if sum in s:
        for i in range(len(l)):
            if l[i] == sum:
                print(len(l[:i]))
                breakpoint=True
                break
    else:
        A = sum
        l.append(sum)
        s.add(sum)
    if breakpoint:
        break