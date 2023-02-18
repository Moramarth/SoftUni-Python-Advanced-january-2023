def index_validator(coordinates):
    row = coordinates[0]
    column = coordinates[1]
    if 0 <= row < number_of_rows and 0 <= column < number_of_columns:
        return True
    return False


def position_change(start_position, direction):
    current_position = [start_position[0], start_position[1]]
    if direction == 'up':
        current_position[0] -= 1
    elif direction == 'down':
        current_position[0] += 1
    elif direction == 'left':
        current_position[1] -= 1
    elif direction == 'right':
        current_position[1] += 1

    return current_position


field_size = input().split()
number_of_rows, number_of_columns = int(field_size[0]), int(field_size[1])

playground = list()
blind_man_position = list()
opponents_count = 3
moves_made = 0

for row_number in range(number_of_rows):
    current_row = input().split()
    if "B" in current_row:
        blind_man_position = [row_number, current_row.index("B")]
    playground.append(current_row)


while True:
    command = input()

    if command == "Finish":
        break

    new_step = position_change(blind_man_position, command)

    if not index_validator(new_step):
        continue
    if playground[new_step[0]][new_step[1]] == "O":
        continue

    if playground[new_step[0]][new_step[1]] == "P":
        opponents_count -= 1
        if opponents_count == 0:
            moves_made += 1
            break

    playground[new_step[0]][new_step[1]] = "B"
    playground[blind_man_position[0]][blind_man_position[1]] = "-"
    blind_man_position = [new_step[0], new_step[1]]
    moves_made += 1

print("Game over!")
print(f"Touched opponents: {3 - opponents_count} Moves made: {moves_made}")

"""
Task conditions are as follows:
Blind man's buff is played in a spacious area, such as outdoors or in a large room, in which one player,
 is blindfolded and gropes around attempting to touch the other players without being able to see them…
 
You will be given N and M – integers, indicating the playground’s dimensions. On the next N lines, you will receive the
rows of the playground, with M columns. You will be marked with the letter 'B', and placed in a random position.

In random positions, furniture or other obstacles will be marked with the letter 'O'.

The other players (opponents) will be marked with the letter 'P'.
There will always be three other players participating in the game.
 
All of the empty positions will be marked with '-'.

Your goal is to touch as many players as possible during the game, without leaving the playground or
stepping on an obstacle.
On the next few lines, until you receive the command "Finish", you will receive a few lines with commands representing
which direction you need to move. The possible directions are "up", " down", "right", and "left".

If the direction leads you out of the field, you need to stay in position inside the field(do NOT make the move).
 
If you have an obstacle, towards the direction, do NOT make the move and wait for the next command.

You need to keep track of the count of touched opponents and the moves you’ve made.

In case you step on a position marked with '-', increase the count of the moves made.

When you receive a command with direction, you check the position you need to step on for an obstacle or opponent.
If there is an opponent, you touch him and the position is marked with '-'(increase the count of the touched opponents
and moves made), and this is your new position. 
The game is over when you manage to touch all other opponents or the given command is "Finish".
A game report is printed on the Console:
"Game over!"
"Touched opponents: {count} Moves made: {count}"

Input
•	On the first line, you'll receive the dimensions of the playground in the format: "N M",
 where N is the number of rows, and M is the number of columns. They'll be separated by a single space (" ").
 
•	On the next N lines, you will receive a string representing the respective row of the playground.
The positions in every string will be separated by a single space (" ").

•	On the next few lines, until you receive the command "Finish", you will be given directions (up, down, right, left). 

Output
•	When the game is over, the following output should be printed on the Console:
"Game over!"
"Touched opponents: {count} Moves made: {count}"
Constraints
•	The playground size will be a 32-bit integer in the range [2 … 2 147 483 647].
•	The playground will always have three opponents in it - 'P'.
•	The obstacles on the playground will always be random count, and there will be cases without any obstacles.

Examples

Input:

5 8
- - - O - P - O
- P - O O - - -
- - - - - - O -
- P B - O - - O
- - - O - - - -
up
up
left
Finish
Output:

Game over!
Touched opponents: 1 Moves made: 3	        

Input:

4 4
O B O -
- P O P
- - P -
- - - - 
left
right
down
right
down
right
up
right
up
down
Finish

Output:
Game over!
Touched opponents: 3 Moves made: 5
"""