for i in range(3):
    Ah, Am, As, Bh, Bm, Bs = map(int, input().split())

    ns = Bs - As
    if ns < 0:
        ns += 60
        Bm -= 1

    nm = Bm - Am
    if nm < 0:
        nm += 60
        Bh -= 1

    nh = Bh - Ah

    print(nh, nm, ns, end=' ')
    print()