N = int(input())

for i in range(N):
    print(' '*(N - i - 1), end='')
    for j in range(i + 1):
        print('*', end='')
        if j != i:
            print(' ', end='')
    print()