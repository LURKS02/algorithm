T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    candy = list(map(int, input().split()))
    result = sum(element // K for element in candy)
    print(result)