def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, element in enumerate(row):
            print("{:d}".format(element), end="")
            if i != len(row) - 1:
                print(" ", end="")
        print()
