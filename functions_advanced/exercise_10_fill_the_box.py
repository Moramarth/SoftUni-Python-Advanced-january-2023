from collections import deque


def fill_the_box(height, length, width, *args):
    box_volume = height * length * width
    space_taken = 0
    commands = args
    cubes_to_place_in_box = deque()
    for command in commands:
        if command == "Finish":
            break
        cubes_to_place_in_box.append(command)

    while cubes_to_place_in_box:
        cube = cubes_to_place_in_box.popleft()

        if box_volume >= space_taken + cube:
            space_taken += cube
            if space_taken == box_volume:
                return f"No more free space! You have {sum(cubes_to_place_in_box)} more cubes."
        else:
            cubes_to_place_in_box.appendleft(abs(box_volume - (space_taken + cube)))
            return f"No more free space! You have {sum(cubes_to_place_in_box)} more cubes."
    else:
        return f"There is free space in the box. You could put {box_volume - space_taken} more cubes."
