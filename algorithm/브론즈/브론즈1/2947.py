l = list(map(int, input().split()))

for i in range(len(l)):
    for j in range(0, len(l) - i - 1):
        if l[j] > l[j + 1]:
            temp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = temp
            for n in l:
                print(n, end= ' ')
            print()