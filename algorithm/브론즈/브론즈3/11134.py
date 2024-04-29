T = int(input())

for _ in range(T):
    N, C = map(int, input().split())

    total = N // C
    if N % C > 0:
        total +=1
    print(total)