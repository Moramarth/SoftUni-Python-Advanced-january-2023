def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_kids = list()
    naughty_kids = list()
    not_found_kids = list()
    santa_filter = {}
    santa_filter_switched = {}
    for key, value in santa_list:
        if key not in santa_filter:
            santa_filter[key] = []
        santa_filter[key].append(value)

    for item in args:
        number, evaluation = item.split("-")
        if int(number) in santa_filter and len(santa_filter[int(number)]) == 1:
            if evaluation == "Nice":
                nice_kids.append(str(santa_filter[int(number)][0]))
            elif evaluation == "Naughty":
                naughty_kids.append(santa_filter[int(number)][0])
            del santa_filter[int(number)]

    for key, value in santa_filter.items():
        for i in range(len(value)):
            if value[i] not in santa_filter_switched:
                santa_filter_switched[value[i]] = []
            santa_filter_switched[value[i]].append(key)

    for key, value in kwargs.items():
        if key in santa_filter_switched and len(santa_filter_switched[key]) == 1:
            if value == "Nice":
                nice_kids.append(key)
            elif value == "Naughty":
                naughty_kids.append(key)
            del santa_filter_switched[key]

    if santa_filter_switched:
        for name in santa_filter_switched.keys():
            for _ in range(len(santa_filter_switched[name])):
                not_found_kids.append(name)

    result = list()
    if nice_kids:
        result.append(f"Nice: {', '.join(nice_kids)}")
    if naughty_kids:
        result.append(f"Naughty: {', '.join(naughty_kids)}")
    if not_found_kids:
        result.append(f"Not found: {', '.join(not_found_kids)}")

    return "\n".join(result)
