T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    h = N % H
    if h == 0:
        h = H
        w = N // H
    else :
        w = N // H + 1
    if w < 10:
        print(f'{h}0{w}')
    else:
        print(f'{h}{w}')