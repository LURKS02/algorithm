S = input()

l = []
for i in range(1, len(S) + 1):
    news = S[-i:]
    l.append(news)
l.sort()
for n in l:
    print(n)