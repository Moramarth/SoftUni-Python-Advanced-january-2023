def shop_from_grocery_list(budget, shopping_list, *args):
    bought_items = list()

    for product in args:
        name = product[0]
        price = float(product[1])
        if name in shopping_list and name not in bought_items:
            if price <= budget:
                bought_items.append(name)
                budget -= price
            else:
                break

    if sorted(bought_items) == sorted(shopping_list):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

    else:
        shopping_list = [product for product in shopping_list if product not in bought_items]
        return f"You did not buy all the products. Missing products: {', '.join(shopping_list)}."


"""
Task conditions are as follows:

John has to shop for products on a list made by his wife. 
You need to help him by writing a program to make his task easier.

Write a function called shop_from_grocery_list that receives information about a budget, a grocery list, products,
and their prices, and returns the result after the shopping. The function will receive a different number of arguments.
The arguments will be passed as follows:
•	The first argument will be the budget - an integer in the range [0, 200];

•	The second argument will be the grocery list - a list with one, many, or no strings representing the products 
needed to be bought;

•	The following arguments will be the tuples with two elements - the first one is the product name (string),
and the second one is its price (float);

After receiving the information and calling the function, the program should start tracking the shopping process:
•	Take the product name from each tuple successively and if you have enough money, buy it, and proceed to the next one.
•	If a product has already been purchased, ignore it, and proceed to the next one.
•	If you receive a product that is not on the grocery list, ignore it, and proceed to the next one.
•	If the budget you have is less than the price of the product, STOP shopping!

 In the end:
•	If you manage to buy all the products from the grocery list, return the message:
"Shopping is successful. Remaining budget: {budget_left}."
The remaining budget should be formatted to the second decimal place.

•	Otherwise, return the message: "You did not buy all the products.
Missing products: {"product1", "product2", …, "product N"}."

Note: Submit only the function in the judge system

Input
•	There will be no input from the console, just parameters passed to your function.
Output
•	Return one of the strings shown above depending on the result. 
Constraints
•	The first argument will always be an integer.
•	The second argument will always be a list.
•	Each tuple given will always contain the product name with its price.


Test code suggestions:

print(shop_from_grocery_list(100, ["tomato", "cola"], ("cola", 5.8),
Shopping is successful. Remaining budget: 84.20.

print(shop_from_grocery_list(100, ["tomato", "cola", "chips", "meat"], ("cola", 5.8), ("tomato", 10.0), ("meat", 22),))
You did not buy all the products. Missing products: chips.

print(shop_from_grocery_list(100, ["tomato", "cola", "chips", "meat", "chocolate"], ("cola", 15.8), ("chocolate", 30),
("tomato", 15.85), ("chips", 50), ("meat", 22.99)))
You did not buy all the products. Missing products: chips, meat.
"""
