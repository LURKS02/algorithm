while(True):
    try:
        s = input()
        a = 0
        b = 0
        c = 0
        d = 0

        for char in s:
            if char.islower():
                a += 1
            if char.isupper():
                b += 1
            if char.isdigit():
                c += 1
            if char.isspace():
                d += 1

        print(a, b, c, d, end= ' ')
        print()

    except EOFError:
        break