N = int(input())

l = list(map(int, input().split()))
B, C = map(int, input().split())

count = 0
for s in l:
    if s < B:
        count += 1
    else :
        if (s - B) % C == 0:
            count += (s - B) // C + 1
        else:
            count += (s - B) // C + 2

print(count)