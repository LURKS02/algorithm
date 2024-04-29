from collections import Counter

N, M, B = map(int, input().split())

l = []
for _ in range(N):
    l += list(map(int, input().split()))

l = Counter(l)

maxh = max(l.keys())
minh = min(l.keys())

time = 99999999999999
height = 0
for i in range(minh, maxh + 1):
    if B + sum((r - i) * l[r] for r in l.keys()) >= 0:
        s = 0
        for n in l.keys():
            if n > i:
                s += 2*(n - i)*l[n]
            elif n < i:
                s += (i - n)*l[n]
        if time >= s:
            time = s
            height = i

print(f'{time} {height}')