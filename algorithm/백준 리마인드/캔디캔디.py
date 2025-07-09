import sys
input = sys.stdin.readline

candies = []
M, N = map(int, input().split())
for _ in range(N):
    candy = int(input())
    candies.append(candy)

candies.sort()

remained = sum(candies) - M
ans = 0

for i in range(N):
    temp = min(candies[i], remained // (N-i))
    ans += temp ** 2
    remained -= temp

print(ans % 2**64)


