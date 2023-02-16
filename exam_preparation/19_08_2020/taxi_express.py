from collections import deque

customers = deque(map(int, input().split(", ")))
taxi_cars = deque(map(int, input().split(", ")))
elapsed_time = 0


while customers and taxi_cars:
    passenger = customers.popleft()
    car = taxi_cars.pop()

    if car >= passenger:
        elapsed_time += passenger
    else:
        customers.appendleft(passenger)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {elapsed_time} minutes")
elif not taxi_cars and customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(passenger) for passenger in customers)}")
