def start_spring(**kwargs):
    spring = kwargs
    spring_switch = dict()
    result = []
    for key, value in spring.items():
        if value not in spring_switch:
            spring_switch[value] = []
        spring_switch[value].append(key)
    for key, value in sorted(spring_switch.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{key}:")
        for item in sorted(value):
            result.append(f"-{item}")

    return "\n".join(result)
