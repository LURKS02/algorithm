from itertools import combinations

N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))

answer = 0

for number in range(2, len(A) + 1): # 15
    for comb in combinations(A, number):
        l = list(comb)
        if sum(l) >= L and sum(l) <= R and max(l) - min(l) >= X:
            answer += 1

print(answer)