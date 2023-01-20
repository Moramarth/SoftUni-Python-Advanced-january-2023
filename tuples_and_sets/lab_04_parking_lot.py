number_of_cars = int(input())

cars_data = [input() for _ in range(number_of_cars)]
cars_in_parking_lot = set()

for info in cars_data:
    command, car = info.split(", ")
    if command == "IN":
        cars_in_parking_lot.add(car)
    elif command == "OUT":
        cars_in_parking_lot.discard(car)


if cars_in_parking_lot:
    print("\n".join(cars_in_parking_lot))
else:
    print("Parking Lot is Empty")
