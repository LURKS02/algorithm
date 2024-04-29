N = int(input())

l = list(map(int, input().split()))
s = set()

for num in l:
    s.add(num)

sortedl = sorted(s)

for num in sortedl:
    print(num, end=' ')