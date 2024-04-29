X = int(input())

B = format(X, 'b')

count = 0
for c in B:
    if c == '1':
        count += 1

print(count)