# for easier testing the file with example text is created here and
# will be deleted when it is no longer needed in Line Numbers task

with open("exercise_01.txt", "w") as source_file:
    source_file.write("-I was quick to judge him, but it wasn't his fault.\n"
                      "-Is this some kind of joke?! Is it?\n"
                      "-Quick, hide here. It is safer.")

raw_text = []
with open("exercise_01.txt", "r") as file_to_read_from:
    for line in file_to_read_from:
        raw_text.append(line)

    for i in range(0, len(raw_text), 2):

        for symbol in {"-", ",", ".", "!", "?"}:
            raw_text[i] = raw_text[i].replace(symbol, "@")

        print(" ".join(raw_text[i].split()[::-1]))
