N, K = map(int, input().split())
l = list(map(int, input().split()))

start = 0
end = 0
count = 0
value = 0
max = -100000000

while((end <= N) and start <= end):
    if count == K:
        if value > max:
            max = value
        count -= 1
        value -= l[start]
        start += 1
    else:
        if end == N:
            break
        value += l[end]
        end += 1
        count += 1

print(max)

