N = int(input())

numbers = list(map(int, input().split()))

lis = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if numbers[i] > numbers[j] and lis[i] < lis[j] + 1:
            lis[i] = lis[j] + 1

lds = [1] * N
for i in reversed(range(N-1)):
    for j in reversed(range(i + 1, N)):
        if numbers[i] > numbers[j] and lds[i] < lds[j] + 1:
            lds[i] = lds[j] + 1

max_length = 0
for i in range(N):
    max_length = max(max_length, lis[i] + lds[i] - 1)

print(max_length)