import itertools

N = int(input())

numbers = [i + 1 for i in range(N)]
permutations = itertools.permutations(numbers)

for perm in permutations:
    print(" ".join(map(str, perm)))