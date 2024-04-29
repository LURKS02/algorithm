N, K = map(int, input().split())

l = [i for i in range(2, N + 1)]

count = 0
while(l):
    min = l[0]
    count += 1
    if count == K:
        print(min)
        break
    l.remove(min)
    breaking = False
    for num in l:
        if num % min == 0:
            count += 1
            if count == K:
                print(num)
                breaking = True
                break
            l.remove(num)
    if breaking:
        break


