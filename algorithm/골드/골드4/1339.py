N = int(input())

words = []

for _ in range(N):
    words.append(input())

weight = {}

for word in words:
    for i, letter in enumerate(reversed(word)):
        if letter in weight:
            weight[letter] += 10**i
        else:
            weight[letter] = 10 ** i

sorted_weights = sorted(weight.items(), key=lambda x: x[1], reverse=True)

number = 9
total_sum = 0

for letter, _ in sorted_weights:
    total_sum += weight[letter] * number
    number -= 1

print(total_sum)