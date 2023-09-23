def safe_print_division(a, b):
    while True:
        try:
            c = a/b
            break
        except ZeroDivisionError:
            c = "None"
        finally:
            print("Inside result:{}".format(c))
