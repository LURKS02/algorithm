N = int(input())

l = []

for _ in range(N):
    name, korean, english, math = input().split()
    l.append((name, int(korean), int(english), int(math)))

l.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in l:
    print(student[0])