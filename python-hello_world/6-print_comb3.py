for i in range(10):
    for j in range(i + 1, 10):
        print("{:d}{:d}".format(i, j), end=", " if j < 9 else "")

print()
