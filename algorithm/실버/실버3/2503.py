from itertools import permutations

N = int(input())

possible_numbers = [''.join(map(str, number)) for number in permutations(range(1, 10), 3)]

def is_valid(number, guess, strike, ball):
    strike_count = sum(n == g for n, g in zip(number, guess))
    ball_count = sum(g in number for g in guess) - strike_count
    return strike_count == strike and ball_count == ball

for _ in range(N):
    guess, strike, ball = input().split()
    strike = int(strike)
    ball = int(ball)

    if strike == 3:
        print(1)
        break

    possible_numbers = {number for number in possible_numbers if is_valid(number, guess, strike, ball)}

else:
    print(len(possible_numbers))