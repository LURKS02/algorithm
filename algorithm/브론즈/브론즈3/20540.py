def MBTI(get):
    if get == 'E':
        return 'I'
    elif get == 'I':
        return 'E'
    elif get == 'S':
        return 'N'
    elif get == 'N':
        return 'S'
    elif get == 'T':
        return 'F'
    elif get == 'F':
        return 'T'
    elif get == 'J':
        return 'P'
    elif get == 'P':
        return 'J'

my = input()
print(''.join(map(MBTI, my)))
