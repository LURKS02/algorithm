import math

N = int(input())
ans = f'{math.factorial(N)}'
for i in range(len(ans)):
    if ans[-(i+1)] != '0':
        print(i)
        break
