def concatenate(*args, **kwargs):
    string = "".join(args)
    to_replace = kwargs
    for key, value in to_replace.items():
        if key in string:
            string = string.replace(key, value)

    return string
