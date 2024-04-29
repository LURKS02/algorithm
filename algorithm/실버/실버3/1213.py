from collections import Counter

ins = input()

c = Counter(ins)

oddl = []
for element in sorted(c):
    if c[element] % 2 != 0:
        oddl.append(element)

if len(oddl) >= 2:
    print("I'm Sorry Hansoo")
else:
    total = []
    for element in sorted(c):
        for _ in range(c[element] // 2):
            total.append(element)
    for c in total:
        print(c, end='')
    if oddl:
        print(oddl[0], end='')
    for c in reversed(total):
        print(c, end='')
