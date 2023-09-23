def safe_print_division(a, b):
    while true:
        try:
            c = a/b
            break
        except ZeroDivisionError:
            c = "None"
        finally:
            print("Inside result:{}".format(c))
