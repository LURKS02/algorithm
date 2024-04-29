N = int(input())

for i in range(N, 3, -1):
    if all(char in ['4', '7'] for char in str(i)):
        print(i)
        break

