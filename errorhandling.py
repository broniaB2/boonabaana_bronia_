while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        result = num1 / num2
        print(f"Result:{result}")
        break
    # exit loop if the operation is successfull
    except ValueError:
        print("invalid input ! please enter numerical values")

    except ZeroDivisionError:
        print("cannot divide by zero .try again")
