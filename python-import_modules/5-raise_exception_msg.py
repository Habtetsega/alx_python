def raise_exception_msg(message=""):
    try :
        raise Exception
    except NameError:
        print(message)
