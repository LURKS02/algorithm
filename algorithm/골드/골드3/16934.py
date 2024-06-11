import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input().rstrip())

nicknames = defaultdict(int)
prefixes = set()

for _ in range(N):
    nickname = input().rstrip()

    found = False
    word = ''
    for c in nickname:
        word += c
        if not found and word not in prefixes:
            print(word)
            found = True
        prefixes.add(word)

    if not found:
        numberOfNickname = nicknames[nickname]
        if numberOfNickname == 0:
            print(nickname)
        else:
            print(nickname + str(numberOfNickname + 1))

    nicknames[nickname] += 1


