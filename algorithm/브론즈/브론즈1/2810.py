N = int(input())
list = input()
lc= list.count('LL')
if lc > 1:
    print(N - lc + 1)
else:
    print(N)