def find_current_weights(G):
    answers = []

    for i in range(1, int(G**0.5) + 1):
        if G % i == 0:
            d = G // i
            if (d + i) % 2 == 0:
                x = (d + i) // 2
                if x**2 - G != 0:
                    answers.append(x)

    if not answers:
        return [-1]
    else:
        return sorted(answers)

G = int(input())
answers = find_current_weights(G)
for ans in answers:
    print(ans)