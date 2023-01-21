random_string = input()

symbol_counter = dict()

for char in random_string:
    if char not in symbol_counter:
        symbol_counter[char] = 0

    symbol_counter[char] += 1

for letter, counter in sorted(symbol_counter.items()):
    print(f"{letter}: {counter} time/s")
    