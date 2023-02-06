text_from_user = input()
try:
    times_to_multiply_text = int(input())
except ValueError:
    print("Variable times(to repeat the text) must be an integer")
else:
    print(text_from_user * times_to_multiply_text)
