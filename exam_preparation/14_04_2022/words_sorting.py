def words_sorting(*args):
    words_dictionary = dict()
    result = list()
    for word in args:
        if word in words_dictionary:
            continue
        words_dictionary[word] = 0
        for char in word:
            words_dictionary[word] += ord(char)

    for key, value in sorted(words_dictionary.items(),
                             key=lambda x: (x[0] if sum(words_dictionary.values()) % 2 == 0 else -x[1])):
        result.append(f"{key} - {value}")

    return "\n".join(result)
