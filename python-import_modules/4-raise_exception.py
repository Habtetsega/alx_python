def raise_exception():
    try:
        raise Exception
    except TypeError as te:
        print("Exeption has been raised")

