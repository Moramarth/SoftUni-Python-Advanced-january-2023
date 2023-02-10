def create(length):
    fibonacci_numbers = list()

    for i in range(length):
        if i == 0:
            fibonacci_numbers.append(i)
        elif i == 1:
            fibonacci_numbers.append(i)
        else:
            fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])

    return fibonacci_numbers


def locate(sequence, number):
    try:
        index = sequence.index(number)
        return f"The number - {number} is at index {index}"
    except ValueError:
        return f"The number {number} is not in the sequence"


