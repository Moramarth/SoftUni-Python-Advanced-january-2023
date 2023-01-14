data = input().split()
rack_capacity = int(input())

number_of_racks_used = 1
sum_of_clothes = 0
current_rack_usage = rack_capacity

clothes = list(map(int, data))

while clothes:
    if clothes[-1] > current_rack_usage:
        current_rack_usage = rack_capacity
        number_of_racks_used += 1
        current_piece = clothes.pop()
        current_rack_usage -= current_piece
        sum_of_clothes += current_piece

    else:
        current_piece = clothes.pop()
        current_rack_usage -= current_piece
        sum_of_clothes += current_piece

print(number_of_racks_used)
