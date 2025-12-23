def operation(operation_type, *args):
    if operation_type == '+':
        total = 0
        for i in args:
            total += i
        print("Sum of numbers:", total)

    elif operation_type == '*':
        total = 1
        for i in args:
            total *= i
        print("Product of numbers:", total)

    else:
        print("Invalid operation")
operation('+', 1, 2, 3)
operation('*', 1, 2, 3, 4)