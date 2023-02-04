def even_odd_filter(**kwargs):
    numbers_dict = dict(kwargs)
    if "even" in numbers_dict:
        numbers_dict["even"] = [num for num in numbers_dict["even"] if num % 2 == 0]
    if "odd" in numbers_dict:
        numbers_dict["odd"] = [num for num in numbers_dict["odd"] if num % 2 != 0]
    sorted_items = sorted(numbers_dict.items(), key=lambda x: -len(x[1]))
    numbers_dict = {key: value for key, value in sorted_items}

    return numbers_dict
