N = int(input())

times = []

for _ in range(N):
    start, end = map(int, input().split())
    times.append((start, end))

times.sort(key=lambda x: (x[1], x[0]))

endTime = 0
count = 0

for (start, end) in times:
    if endTime <= start:
        endTime = end
        count += 1

print(count)