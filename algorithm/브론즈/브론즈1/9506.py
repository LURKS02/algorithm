while(True):
    N = int(input())
    if N == -1:
        break
    else:
        l = []
        for i in range(N - 1):
            if N % (i+1) == 0:
                l.append(i + 1)

        if sum(l) == N:
            print(f'{N} = ', end='')
            for i in range(len(l)):
                print(l[i], end='')
                if i != len(l) -1:
                    print(' + ', end='')
        else:
            print(f'{N} is NOT perfect.', end='')
        print()