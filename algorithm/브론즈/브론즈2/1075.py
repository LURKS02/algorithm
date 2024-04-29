N = int(input())
F = int(input())

N = (N // 100) * 100

while(True):
    if N % F == 0:
        print(str(N)[-2:])
        break
    else:
        N += 1