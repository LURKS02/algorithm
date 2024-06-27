import sys

N = int(input())

h = list(map(int, input().split()))
h.sort()

ans = sys.maxsize

for i in range(N):
    for j in range(i+3, N):
        left, right = i+1, j-1
        while left < right:
            temp = (h[i] + h[j]) - (h[left] + h[right])
            if abs(ans) > abs(temp):
                ans = abs(temp)
            if temp < 0:
                right -= 1
            else:
                left += 1
print(ans)