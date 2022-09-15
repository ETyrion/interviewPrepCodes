def add_numbers(num1, num2, operation):
    if operation == "add":
        result = num1+num2

    elif operation == "subtract":
        result = num1 - num2

    elif operation == "mutiply":
        result = num1*num2

    elif operation == "div":
        result = num1/num2

    print("Result "+str(result))

add_numbers(3,4, "subtract")