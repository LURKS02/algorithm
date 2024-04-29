a, b, c, d, e, f = map(int, input().split())

print(int((c*e - f*b) / (a*e - b*d)), int((c*d - a*f) / (b*d - a*e)), end = ' ')