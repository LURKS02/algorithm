def rev(N):
    return N[::-1]

X, Y = input().split()
r = f"{int(rev(X)) + int(rev(Y))}"
print(int(rev(r)))
