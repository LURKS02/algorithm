N = int(input())
alpas = [[0, False] for _ in range(10)]
ans = 0

for _ in range(N):
    string = input()
    alpas[ord(string[0])-65][1] = True

    m = 1
    for c in range(len(string)-1, -1, -1):
        alpas[ord(string[c])-65][0] += m
        m *= 10

alpas.sort(reverse=True)

if alpas[9][1]:
    for i in range(8, -1, -1):
        if not alpas[i][1]:
            del alpas[i]
            break

for i in range(9):
    ans += alpas[i][0] * (9-i)

print(ans)
