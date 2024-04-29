cases = {'A': 300, 'B': 60, 'C': 10}

N = int(input())

a = N // cases['A']
N = N % cases['A']

b = N // cases['B']
N = N % cases['B']

c = N // cases['C']
N = N % cases['C']

if N != 0:
    print(-1)
else:
    print(a, b, c, end=' ')