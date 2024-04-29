N = int(input())
l = []

for i in range(N):
    l.append(input())

found = False

for i in range(len(l)):
    if found:
        break
    for j in range(len(l)):
        if l[i] == l[j][::-1]:
            print(len(l[i]), l[i][len(l[i]) // 2])
            found = True
            break

