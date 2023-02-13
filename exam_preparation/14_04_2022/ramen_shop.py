from collections import deque

bowls_of_ramen = deque(map(int, input().split(", ")))
customers = deque(map(int, input().split(", ")))

while bowls_of_ramen and customers:
    current_bowl = bowls_of_ramen.pop()
    current_customer = customers.popleft()

    if current_customer == current_bowl:
        continue
    elif current_customer < current_bowl:
        current_bowl -= current_customer
        bowls_of_ramen.append(current_bowl)
    elif current_customer > current_bowl:
        current_customer -= current_bowl
        customers.appendleft(current_customer)

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(bowl) for bowl in bowls_of_ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(customer) for customer in customers)}")
