def func_executor(*args):
    result = list()
    for func, value in args:
        result.append(f"{func.__name__} - {func(*value)}")

    return "\n".join(result)
