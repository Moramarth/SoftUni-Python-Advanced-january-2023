def list_manipulator(list_of_numbers, command, direction, *args):

    if args:
        if command == "add":
            if direction == "end":
                list_of_numbers.extend(args)
            else:
                for element in reversed(args):
                    list_of_numbers.insert(0, element)
        else:
            if direction == "end":
                for _ in range(args[0]):
                    list_of_numbers.pop()
            else:
                for _ in range(args[0]):
                    list_of_numbers.pop(0)
    else:
        if direction == "end":
            list_of_numbers.pop()
        else :
            list_of_numbers.pop(0)

    return list_of_numbers
