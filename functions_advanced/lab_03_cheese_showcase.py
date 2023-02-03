def sorting_cheeses(**cheese_dictionary):
    cheese_dictionary = sorted(cheese_dictionary.items(), key=lambda x: (-len(x[1]), x[0]))
    result = list()

    for cheese_name, quantity in cheese_dictionary:
        result.append(cheese_name)
        quantity_list = sorted(quantity, reverse=True)
        result += quantity_list

    return "\n".join(list(map(str, result)))
