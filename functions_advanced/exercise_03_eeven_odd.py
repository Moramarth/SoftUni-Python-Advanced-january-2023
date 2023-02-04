def even_odd(*args):
    sequence = list(args)
    command = sequence.pop()
    numbers = [int(num) for num in sequence]
    if command == "even":
        return [num for num in numbers if num % 2 == 0]
    elif command == "odd":
        return [num for num in numbers if num % 2 != 0]
