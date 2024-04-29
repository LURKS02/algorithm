s = input()

def making(char):
    if char.isupper():
        new = ord(char) + 13
        if new > 90:
            new -= 26
        return chr(new)
    elif char.islower():
        new = ord(char) + 13
        if new > 122:
            new -= 26
        return chr(new)
    elif char.isdigit:
        return char
    else:
        return ' '


for c in s:
    print(making(c), end ='')