def shopping_cart(*args):
    ingredients = {
        "Soup": list(),
        "Pizza": list(),
        "Dessert": list(),
    }
    final_report = []

    for item in args:
        if item == "Stop":
            break
        if item[1] not in ingredients[item[0]]:
            if item[0] == "Soup" and len(ingredients["Soup"]) == 3:
                continue

            elif item[0] == "Pizza" and len(ingredients["Pizza"]) == 4:
                continue

            elif item[0] == "Dessert" and len(ingredients["Dessert"]) == 2:
                continue

            ingredients[item[0]].append(item[1])

    if not ingredients["Soup"] and not ingredients["Pizza"] and not ingredients["Dessert"]:
        return "No products in the cart!"

    products_in_cart = sorted(ingredients.items(), key=lambda x: (-len(x[1]), x[0]))

    for meal, ingredient in products_in_cart:
        final_report.append(f"{meal}:")
        for item in sorted(ingredient):
            final_report.append(f" - {item}")

    return "\n".join(final_report)
