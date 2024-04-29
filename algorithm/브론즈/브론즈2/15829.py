L = int(input())
s = input()

l = []
for c in s:
    l.append(ord(c) - 96)

count = 0
for i in range(len(l)):
    count += l[i] * pow(31, i)

print(count % 1234567891)