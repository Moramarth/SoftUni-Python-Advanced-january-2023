from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

desired_words = ["rose", "tulip", "lotus", "daffodil"]
found_letters = {
    "rose": [],
    "tulip": [],
    "lotus": [],
    "daffodil": [],
}
word_is_found = False

while vowels and consonants:
    test_vowel = vowels.popleft()
    test_consonant = consonants.pop()
    for word in desired_words:
        if test_vowel in word:
            found_letters[word].append(test_vowel)
        if test_consonant in word:
            found_letters[word].append(test_consonant)
        if len(set(word)) == len(set(found_letters[word])):
            word_is_found = True
            print(f"Word found: {word}")
            break
    if word_is_found:
        break

else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
