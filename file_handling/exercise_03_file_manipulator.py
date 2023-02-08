import os

try:
    os.remove("exercise_02_output.txt")
except FileNotFoundError:
    print("An error has occurred. You have already deleted 'exercise_02_output.txt'.")

