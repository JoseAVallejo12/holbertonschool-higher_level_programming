def safe_print_division(a, b):
    try:
        result = int(a / b)
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: ".format(a, b, result))
    return result
