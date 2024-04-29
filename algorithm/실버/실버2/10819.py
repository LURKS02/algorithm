from itertools import permutations

N = int(input())
l = list(map(int, input().split()))

p = list(permutations(l, N))

max = 0
for list in p:
    value = sum(abs(list[n] - list[n - 1]) for n in range(1, N))
    if max < value:
        max = value
print(max)