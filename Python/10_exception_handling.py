try:
    number=int(input("Enter a number: "))
    result=100/number
    print("Result", result)

except ValueError:
    print("Enter a Valid Number")

except ZeroDivisionError:
    print("You cannot devide By Zero")