def palindrome(word, starting_index, ending_index=-1):
    if starting_index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[starting_index] != word[ending_index] :
        return f"{word} is not a palindrome"

    return palindrome(word, starting_index + 1, ending_index - 1)
