from functools import reduce

random_sequence = input().split()

operators = "*/-+"
index = 0
calculations = {
    "*": lambda i: reduce(lambda x, y: int(x) * int(y), random_sequence[:i]),
    "/": lambda i: reduce(lambda x, y: int(x) / int(y), random_sequence[:i]),
    "+": lambda i: reduce(lambda x, y: int(x) + int(y), random_sequence[:i]),
    "-": lambda i: reduce(lambda x, y: int(x) - int(y), random_sequence[:i]),
}

while index < len(random_sequence):
    current_element = random_sequence[index]
    if current_element in operators:
        result = calculations[current_element](index)

        for _ in range(index):
            random_sequence.pop(1)
        random_sequence[0] = result
        index = 0
    index += 1

print(int(random_sequence[0]))
