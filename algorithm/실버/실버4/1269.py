N, M = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

a = A - B
b = B - A

ans = a | b

print(len(ans))