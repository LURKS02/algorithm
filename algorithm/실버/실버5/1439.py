S = input()

i = 0

zerocount = 0
onecount = 0

while(i < len(S)):
    if S[i] == '0':
        while i < len(S) and S[i] == '0':
            i += 1
        zerocount += 1
    else:
        while i < len(S) and S[i] == '1':
            i += 1
        onecount += 1

print(min(zerocount, onecount))