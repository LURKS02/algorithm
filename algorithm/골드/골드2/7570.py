N = int(input())
children = list(map(int, input().split()))
idx = [-1] * N

for i in range(N):
    idx[children[i] - 1] = i

# print(idx)

num = 1
max_lis = 1

for i in range(N - 1):
    if idx[i] < idx[i+1]:
        num += 1
        max_lis = max(max_lis, num)

    else:
        num = 1

print(N - max_lis)