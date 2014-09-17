try:
    number1 = int(input("Enter number 1: "))
    number2 = int(input("Enter number 2: "))
    div = number1 // number2
    mod = number1 % number2
    print("The integer result of the division is {}".format(div))
    print("The remainder of the division is {}".format(mod))
except ValueError:
    print("The numbers need to be integers")
except ZeroDivisionError:
    print("The second number cannot be 0")

