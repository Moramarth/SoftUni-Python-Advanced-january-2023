import os
from string import punctuation

try:
    with open("exercise_01.txt", "r") as file_to_read_from:
        data = list()
        for line in file_to_read_from:
            data.append(line)
except FileNotFoundError:
    print(("An error has occurred,you are missing 'file exercise_01.txt'!\n"
           "Please run 'exercise_01_even_lines.py' to create it and continue testing."))
os.remove("exercise_01.txt")

# file created here will be deleted in the next task
with open("exercise_02_output.txt", "w") as updated_text_file:
    for i in range(len(data)):
        letters_count = 0
        symbols_count = 0
        for char in data[i]:
            if char.isalpha():
                letters_count += 1
            elif char in punctuation:
                symbols_count += 1
        updated_text_file.write(f"Line {i+1}: {data[i][:-1]} ({letters_count})({symbols_count})\n")
