T = int(input())

for i in range(T):
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    print(l[2])