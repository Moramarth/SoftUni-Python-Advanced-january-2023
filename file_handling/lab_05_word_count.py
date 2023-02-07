from re import findall

word_counter = dict()

with open("words.txt") as first_file:
    words_to_count = first_file.readline().split()

for word in words_to_count:
    word_counter[word] = 0

with open("text_for_task_5.txt") as second_file:
    data = findall("[A-Za-z]+", second_file.read())
    data = [word.lower() for word in data]
    for word in data:
        if word in words_to_count:
            word_counter[word] += 1

sorted_words = sorted(word_counter.items(), key=lambda x: -x[1])
for item in sorted_words:
    print(f"{item[0]} - {item[1]}")
