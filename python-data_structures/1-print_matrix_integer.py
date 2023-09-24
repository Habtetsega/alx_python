def print_matrix_integer(matrix=[[]]):
    r=len(matrix)
    c=len(matrix[0])
    for i in range(r):
        j=0
        print("{:d}{:d}{:d}\n".format(matrix[i][j],matrix[i][j+1],matrix[i][j+2]))
        j+=1
