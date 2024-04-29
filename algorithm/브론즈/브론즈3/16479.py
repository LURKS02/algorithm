K = int(input())
D1, D2 = map(int, input().split())

result = pow(K, 2) - pow((D1-D2)/2, 2)

if result.is_integer():
    print(int(result))

else:
    print(result)