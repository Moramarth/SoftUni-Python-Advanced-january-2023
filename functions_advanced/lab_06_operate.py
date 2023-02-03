from functools import reduce


def operate(operator, *args):
    if operator == "+":
        return sum(args)
    if operator == "-":
        return reduce(lambda x, y: x - y, list(args))
    if operator == "*":
        if 0 in args:
            return 0
        return reduce(lambda x, y: x * y, list(args))
    if operator == "/":
        if 0 in args:
            return 0
        return reduce(lambda x, y: x / y, list(args))
