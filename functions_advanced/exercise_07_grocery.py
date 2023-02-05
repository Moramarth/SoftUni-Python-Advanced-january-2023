def grocery_store(**kwargs):
    grocery_data = kwargs
    sorted_list = sorted(grocery_data.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []
    for item in sorted_list:
        result.append(f"{item[0]}: {item[1]}")
    return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
    apple=2,
    corns=2,
    dogss=2
))
