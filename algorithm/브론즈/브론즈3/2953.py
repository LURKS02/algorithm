max = 0
person = 0
for i in range(5):
    A = sum(map(int, input().split()))
    if max < A:
        max = A
        person = i + 1

print(person, max, end = ' ')