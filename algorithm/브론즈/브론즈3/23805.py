N = int(input())

for i in range(N):
    print('@@@' * N + ' ' * N + '@' * N)

for i in range(N * 3):
    print('@' * N + ' ' * N + '@' * N + ' ' * N + '@' * N)

for i in range(N):
    print('@' * N + ' ' * N + '@@@' * N)