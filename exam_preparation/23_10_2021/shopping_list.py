def shopping_list(money, **kwargs):
    result = []
    if money < 100:
        return "You do not have enough budget."

    for item, value in kwargs.items():
        cost = float(value[0]) * int(value[1])
        if money >= cost:
            money -= cost
            result.append(f"You bought {item} for {cost:.2f} leva.")
        if len(result) == 5:
            break

    return "\n".join(result)
