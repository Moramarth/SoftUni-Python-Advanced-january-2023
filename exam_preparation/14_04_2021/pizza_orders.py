from collections import deque

pizza_orders = deque(map(int, input().split(", ")))
employee_capacity = deque(map(int, input().split(", ")))

total_pizzas_made = 0

while pizza_orders and employee_capacity:
    order = pizza_orders.popleft()
    if order <= 0 or order > 10:
        continue

    chef = employee_capacity.pop()
    if order > chef:
        order -= chef
        total_pizzas_made += chef
        pizza_orders.appendleft(order)
        continue

    total_pizzas_made += order

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_made}")
    print(f"Employees: {', '.join(str(chef) for chef in employee_capacity)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(order) for order in pizza_orders)}")
