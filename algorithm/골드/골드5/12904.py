S = input()
T = input()

while len(T) > len(S):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1][::-1]

if S == T:
    print(1)
else:
    print(0)