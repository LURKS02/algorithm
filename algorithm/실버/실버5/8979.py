N, K = map(int, input().split())

scores = []

for i in range(N):
    country, gold, silver, bronze = map(int, input().split())
    scores.append((country, gold, silver, bronze))

sorted_scores = sorted(scores, key = lambda x: (-x[1], -x[2], -x[3]))

ranks = [0] * 1000

rank = 1

previous = None
for index, (country, gold, silver, bronze) in enumerate(sorted_scores, start = 1):
    if previous != (gold, silver, bronze):
        rank = index
    previous = (gold, silver, bronze)
    ranks[country - 1] = rank
print(ranks[K - 1])