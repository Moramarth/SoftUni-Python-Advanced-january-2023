def math_operations(string):
    first_number, second_number, symbol = float(string.split()[0]), float(string.split()[2]), string.split()[1]
    if symbol == "+":
        result = first_number + second_number
    elif symbol == "-":
        result = first_number - second_number
    elif symbol == "*":
        result = first_number * second_number
    elif symbol == "/":
        if first_number == 0 or second_number == 0:
            return "Forbidden division by 0"
        result = first_number / second_number
    elif symbol == "^":
        result = first_number**second_number
    else:
        return "Please enter a valid operator"

    return f"{result:.2f}"
