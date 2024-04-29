now = 0
max = 0
for i in range(4):
    a, b = map(int, input().split())
    now = now - a + b
    if max < now:
        max = now

print(max)