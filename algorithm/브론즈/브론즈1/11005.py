def radixChange(num, radix):
    if num == 0:
        return '0'

    nums = []
    while num:
        num, digit = divmod(num, radix)
        if digit >= 10:
            nums.append(chr(digit + 55))
        else:
            nums.append(str(digit))

    return ''.join(reversed(nums))

N, B = map(int, input().split())
print(radixChange(N, B))