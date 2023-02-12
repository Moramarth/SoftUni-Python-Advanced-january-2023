from collections import deque

seats_list = input().split(", ")
fifo_sequence = deque(map(int, input().split(", ")))
lifo_sequence = deque(map(int, input().split(", ")))

seats_taken = list()
rotations_count = 0

while True:
    if len(seats_taken) > 2:
        break
    if rotations_count > 9:
        break
    rotations_count += 1
    first_num = fifo_sequence.popleft()
    second_num = lifo_sequence.pop()
    result = chr(first_num + second_num)
    if str(first_num) + result in seats_list:
        if str(first_num) + result not in seats_taken:
            seats_taken.append(str(first_num) + result)
        else:
            continue
    elif str(second_num) + result in seats_list:
        if str(second_num) + result not in seats_taken:
            seats_taken.append(str(second_num) + result)
        else:
            continue
    else:
        fifo_sequence.append(first_num)
        lifo_sequence.appendleft(second_num)

print(f"Seat matches: {', '.join(seats_taken)}")
print(f"Rotations count: {rotations_count}")
