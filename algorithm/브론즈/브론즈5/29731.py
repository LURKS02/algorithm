list = ['Never gonna give you up',
        'Never gonna let you down',
        'Never gonna run around and desert you',
        'Never gonna make you cry',
        'Never gonna say goodbye',
        'Never gonna tell a lie and hurt you',
        'Never gonna stop']

N = int(input())
trueResult = True

for _ in range(N):
    str = input()
    if not str in list:
        trueResult = False

if trueResult:
    print('No')
else:
    print('Yes')
