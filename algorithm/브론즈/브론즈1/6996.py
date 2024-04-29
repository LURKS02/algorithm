T = int(input())

for i in range(T):
    A, B = input().split()
    if len(A) != len(B):
        print(f'{A} & {B} are NOT anagrams.')
    else:
        if sorted(A) == sorted(B):
            print(f'{A} & {B} are anagrams.')
        else:
            print(f'{A} & {B} are NOT anagrams.')