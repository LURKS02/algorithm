N, K = map(int, input().split())

temp = [0] * 1000002

for _ in range(N):
    A, B = map(int, input().split())
    temp[A+1] += 1
    temp[B+1] -= 1

for i in range(1, 1000001):
    temp[i] += temp[i-1]

start = 0
end = 1
value = temp[1]

while start <= end and end < 1000002:
    if value == K:
        print(start, end)
        exit(0)

    elif value < K:
        end += 1
        if end < 1000002:
            value += temp[end]

    else:
        value -= temp[start+1]
        start += 1

print(0, 0)
