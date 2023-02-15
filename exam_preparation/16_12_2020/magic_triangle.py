def get_magic_triangle(number_of_rows):
    magic = [[1], [1, 1]]
    for i in range(2, number_of_rows):
        magic.append([])
        for j in range(i + 1):
            left_neighbour = 0
            if 0 <= j - 1:
                left_neighbour = magic[i - 1][j - 1]
            right_neighbour = 0
            if len(magic[i - 1]) > j:
                right_neighbour = magic[i - 1][j]
            number = left_neighbour + right_neighbour
            magic[i].append(number)

    return magic
