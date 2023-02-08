import os

try:
    os.remove("exercise_02_output.txt")
except FileNotFoundError:
    print("An error has occurred. You have already deleted 'exercise_02_output.txt'.")

data = input()
while data != "End":

    command, file_name, *additional_info = data.split("-")

    if command == "Create":
        desired_file = open(file_name, "w")
        desired_file.close()

    elif command == "Add":
        content = additional_info[0]

        file_to_add_data = open(file_name, "a")
        file_to_add_data.write(content + "\n")
        file_to_add_data.close()

    elif command == "Replace":
        old_string, new_string = additional_info[0], additional_info[1]

        try:
            with open(file_name, "r") as file_to_replace_data:
                text_in_file = file_to_replace_data.read()

            text_in_file = text_in_file.replace(old_string, new_string)

            with open(file_name, "w") as file_to_replace_data:
                file_to_replace_data.write(text_in_file)

        except FileNotFoundError:
            print("An error occurred.")

    elif command == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred.")

    data = input()
