A, B = map(int, input().split())
m = int(input())
l = list(map(int, input().split()))
l.reverse()

sum = 0
for i in range(m):
    index = pow(A, i)
    sum += l[i] * index

nums = []
while(sum):
    sum, digit = divmod(sum, B)
    nums.append(digit)
nums.reverse()
for num in nums:
    print(num, end=' ')