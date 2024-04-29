n = int(input())

s = set()
for _ in range(n):
    A, B = input().split()
    if B == 'enter':
        s.add(A)
    else:
        s.remove(A)

l = sorted(s, reverse=True)

for name in l:
    print(name)