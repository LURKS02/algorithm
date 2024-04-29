n = int(input())

persons = []

for _ in range(n):
    name, day, month, year = input().split()
    persons.append((name, int(day), int(month), int(year)))

sortedPersons = sorted(persons, key = lambda x: (-x[3], -x[2], -x[1]))
high = sortedPersons[n - 1]
low = sortedPersons[0]

print(low[0])
print(high[0])