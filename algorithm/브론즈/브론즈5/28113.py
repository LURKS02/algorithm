N, A, B = map(int, input().split())

if A < B:
    print('Bus')
elif A == B:
    print('Anything')
else:
    print('Subway')