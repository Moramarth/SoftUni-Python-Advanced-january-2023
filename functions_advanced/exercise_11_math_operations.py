def math_operations(*args, **kwargs):
    for i in range(len(args)):
        current_key = list(kwargs)[i % 4]

        if current_key == "a":
            kwargs[current_key] += args[i]
        elif current_key == "s":
            kwargs[current_key] -= args[i]
        elif current_key == "d":
            if args[i] != 0:
                kwargs[current_key] /= args[i]
        elif current_key == "m":
            kwargs[current_key] *= args[i]

    result_list = sorted(kwargs.items(), key=lambda x: (-x[1], x[1]))
    desired_format = list()
    for item in result_list:
        desired_format.append(f"{item[0]}: {item[1]:.1f}")

    return "\n".join(desired_format)
