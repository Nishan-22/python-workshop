def division(): 
    val = int(input("Enter a division"))
    try:
        quotient = 100 / val
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print("Quotient is:", quotient)
    finally:
        print("Process Completed")