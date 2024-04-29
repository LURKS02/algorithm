a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())

sumA = a + b + c + d
sumB = e + f + g + h

if sumA>=sumB:
    print(sumA)
else:
    print(sumB)