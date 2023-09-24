def print_matrix_integer(matrix=[[]]):
    r=len(matrix)
    c=len(matrix[0])
    for i in range(r):
        for j in range(c):
            print("{:d}".format(matrix[i][j]),end="")
        print()
