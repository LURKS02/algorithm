N = int(input())

l = list(map(int, input().split()))

M = 0
Y = 0

for item in l:
    M += (item // 60 + 1) * 15
    Y += (item // 30 + 1) * 10

if M > Y:
    print(f'Y {Y}')
elif M < Y:
    print(f'M {M}')
else:
    print(f'Y M {Y}')