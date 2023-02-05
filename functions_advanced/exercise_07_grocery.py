def grocery_store(**kwargs):
    grocery_data = kwargs
    sorted_list = sorted(grocery_data.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []
    for item in sorted_list:
        result.append(f"{item[0]}: {item[1]}")
    return "\n".join(result)
