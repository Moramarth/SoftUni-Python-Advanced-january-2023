random_numbers = list(map(float, input().split()))

number_counter = dict()

for number in random_numbers:
    if number not in number_counter:
        number_counter[number] = 0

    number_counter[number] += 1

for key, value in number_counter.items():
    print(f"{key} - {value} times")
