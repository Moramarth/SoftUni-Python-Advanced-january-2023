from collections import deque

textiles_values = deque(map(int, input().split()))
medicament_values = deque(map(int, input().split()))

crafting_recipes = {
    "Patch":	30,
    "Bandage":	40,
    "MedKit": 	100,
}

crafted_items = {
    "Bandage":	0,
    "MedKit": 	0,
    "Patch":	0,
}

while textiles_values and medicament_values:
    textile = textiles_values.popleft()
    medicament = medicament_values.pop()

    mix = textile + medicament
    if mix in [30, 40, 100]:
        for key, value in crafting_recipes.items():
            if value == mix:
                crafted_items[key] += 1
    elif mix > 100:
        crafted_items["MedKit"] += 1
        medicament_values[-1] += mix - 100
    else:
        medicament += 10
        medicament_values.append(medicament)

if not textiles_values and not medicament_values:
    print("Textiles and medicaments are both empty.")
elif not textiles_values:
    print("Textiles are empty.")
elif not medicament_values:
    print("Medicaments are empty.")


result = sorted(crafted_items.items(), key=lambda x: (-x[1], x[0]))


for item in result:
    if int(item[1]) > 0:
        print(f"{item[0]} - {item[1]}")


if textiles_values:
    print(f"Textiles left: {', '.join(str(textile) for textile in textiles_values)}")
if medicament_values:
    print(f"Medicaments left: {', '.join(str(medicament) for medicament in reversed(medicament_values))}")


"""
Task conditions are as follows:
You are in the middle of a zombie apocalypse and you want to go out for exploration. But before you do that,
you need to prepare some healing items.

On the first line, you will be given a sequence representing textiles.
On the second line, you will be given another sequence, which represents medicaments.

While both collections contain any elements, you will have to combine elements from the collections in order to create
 healing items. You should start by getting the first value of textile and the last value of medicaments:
•	If their sum is equal to any of the items in the table below create that item and remove both values.

•	Otherwise, check if the sum is bigger than the value of the MedKit, create the MedKit, remove both values,
 and add the remaining resources(of the sum) to the next value in the medicament collection (Take the element from the
  collection, add the remaining sum to it, and put the element back to its place).

•	If you can’t create anything, remove the textile value, add 10 to the medicament value,
 and return the medicament back to its place, into its collection.

You need to stop creating healing items when either the textile or the medicaments are exhausted.

Healing item	Resources needed
Patch	        30
Bandage	        40
MedKit	        100

In the end, you should print on the console message for the sequence that has ended, then the created items,
 and in the end the remaining items (if any).

Input
•	On the first line, you will receive a sequence of integers representing the textiles, separated by a single space.
•	On the second line, you will receive a sequence of integers representing the medicaments,
 separated by a single space.

Output
•	On the first line print which one of the collections is over:
o	If the textile is over print: "Textiles are empty."
o	If the medicaments are over print: "Medicaments are empty."
o	If both are empty print: "Textiles and medicaments are both empty."
•	On the next n lines print only the created items (if any) ordered by the amount created descending,
 then by name alphabetically:

"{item name} - {amount created}
  {item name} - {amount created}
…
"

Hint: Do not print items, which are not created.
•	On the last line print the remaining items(if any):
o	If there are any medicaments left:
 "Medicaments left: …{medicament2}, {medicament1}"
o	If there are any textiles left:
"Textiles left: {textile1}, {textile2}…"
Constraints
•	All the numbers will be in the range [0…1000].
•	All the inputs will be valid.

Examples:
Input	            Output

20 10 40 70 20      Textiles are empty.
10 50 10 30 20 80	MedKit - 2
                    Bandage - 1
                    Patch - 1
                    Medicaments left: 50, 10
                    
                    
30 30 10 80 60      Textiles and medicaments are both empty.
40 20 30 10 70	    MedKit - 3
                    Bandage - 2



30 30 10 80 60 20   Medicaments are empty.
40 20 30 10 70	    MedKit - 3
                    Bandage - 2
                    Textiles left: 20
                    

60 15 20 30 20      Medicaments are empty.
20 15 40	        Bandage - 1
                    MedKit - 1
                    Patch - 1
                    Textiles left: 30, 20
"""
