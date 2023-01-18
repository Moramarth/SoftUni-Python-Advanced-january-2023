from _collections import deque

green_light_duration = int(input())
free_window_for_exit_only = int(input())

COMMAND_GREEN = "green"
COMMAND_END = "END"

car_count = 0

cars_at_traffic_light = deque()

while True:
    car_model = input()
    if car_model == COMMAND_END:
        break
    if car_model != COMMAND_GREEN:
        cars_at_traffic_light.append(car_model)
    else:
        timer = green_light_duration
        while timer > 0 and cars_at_traffic_light:
            current_car = cars_at_traffic_light.popleft()

            total_time_to_pass = timer + free_window_for_exit_only

            if len(current_car) > total_time_to_pass:
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[total_time_to_pass]}.")
                exit()

            timer -= len(current_car)
            car_count += 1

print("Everyone is safe.")
print(f"{car_count} total cars passed the crossroads.")
