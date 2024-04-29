T = int(input())

for i in range(T):
    l = list(input().split(' '))
    for s in l:
        print(s[::-1], end= ' ')

    print()