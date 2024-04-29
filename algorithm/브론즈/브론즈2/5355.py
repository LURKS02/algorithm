T = int(input())

for i in range(T):
    l = list(input().split())
    sum = 1
    for i in range(len(l)):
        if i == 0:
            sum = float(l[i])
        else:
            if l[i] == '@':
                sum *= 3
            elif l[i] == '%':
                sum += 5
            else:
                sum -= 7

    print(format(sum, '.2f'))