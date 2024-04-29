N = int(input())
Slen = int(input())
S = input()

count = 0
pattern = 0
i = 1

while i < Slen-1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        pattern += 1
        if pattern == N:
            pattern -= 1
            count += 1
        i += 1
    else:
        pattern = 0
    i += 1

print(count)