N = int(input())

times = list(map(int, input().split()))
total = sum(times) + 8 * (N - 1)

h = total // 24
m = total % 24

print(h, m, end= ' ')