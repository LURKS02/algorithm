N = int(input())

for i in range(N):
    print('*' * (i + 1), end='')
    print(' '* 2*(N - i - 1), end='')
    print('*' * (i + 1), end='')
    print()

for i in range(N-1):
    print('*' * (N-1-i), end='')
    print(' ' * 2*(i + 1), end='')
    print('*' * (N - 1 - i), end='')
    print()