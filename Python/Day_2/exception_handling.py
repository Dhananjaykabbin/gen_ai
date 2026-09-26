def divide_numbers(a, b):
    try:
        result = a / b

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation completed.")


divide_numbers(10, 2)
divide_numbers(10, 0)