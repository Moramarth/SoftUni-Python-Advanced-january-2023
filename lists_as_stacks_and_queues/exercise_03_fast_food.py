from _collections import deque

food_quantity = int(input())

data = list(map(int, input().split()))
print(max(data))

orders = deque(data)

for order in range(len(orders)):
    if food_quantity < orders[0]:
        break
    else:
        food_quantity -= orders.popleft()

if not orders:
    print("Orders complete")
else:
    orders_left = list(map(str, orders))
    print(f"Orders left: {' '.join(orders_left)}")
