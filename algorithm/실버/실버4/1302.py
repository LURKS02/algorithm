N = int(input())

dict = {}

for _ in range(N):
    book = input()
    if book in dict:
        dict[book] += 1
    else:
        dict[book] = 1

maxbook = max(dict.values())
maxkeys = [k for k, v in dict.items() if v == maxbook]
print(min(maxkeys))