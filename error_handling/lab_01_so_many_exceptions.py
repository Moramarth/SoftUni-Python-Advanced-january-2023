"""
Original Code for review:

numbers_list = int(input()).split(", ")
result = 1

for i in range(numbers_list):
    number = numbers_list[i+1]
    if number <= 5
        result *= number
    elif 5 < number <= 10:
        result /= number

print(total)
"""
# We split before we cast items to int.
# Can also be done with comprehension using map_function again or int(number) for number in input().split(", ")
numbers_list = input().split(", ")
numbers_list = list(map(int, numbers_list))
result = 1

# range takes only integer values so we need to use the length of list not the list itself
for i in range(len(numbers_list)):
    number = numbers_list[i]  # index error occurring => i+1 goes outside of range also skips index 0
    if number <= 5:  # missing semi-column after if statement
        result *= number
    elif 5 < number <= 10:
        result /= number

# Variable "total" is not defined. All calculations are stored in the variable "result".
# Casting "result" to float is necessary for only one of the expected test outputs.
print(float(result))
