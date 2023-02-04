number_sequence = list(map(int, input().split()))

negatives = 0
positives = 0

for number in number_sequence:
    if number > 0:
        positives += number
    else:
        negatives += number

print(negatives)
print(positives)

if positives > abs(negatives):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
