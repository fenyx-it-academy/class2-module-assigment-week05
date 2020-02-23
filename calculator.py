text =("""
Choose the operation you want to do:
1- Addition
2- Subtracting 
3- Multiplying
4- division
""")

while True:
    firstNumber = input("Type first number: ")
    secondNumber = input("Type second number: ")

    try:
        a = int(firstNumber)
        b = int(secondNumber)
    except ValueError:
        print("Type a number only.")
        print("Exit the program...")
        break

    operationTime = input(text)
    try:
        c = int(operationTime)
    except ValueError:
        print("1 - 2 - 3 - 4 You can't type without these numbers.")
        print("Exit the program...")
        break
        
    if c == 1:
        print("Result of addition : " , a + b)

    elif c == 2:
        print("Result of subtracting : " , a - b)

    elif c == 3:
        print("Result of multiplying : " , a * b)

    elif c == 4:
        if b == 0:
            print("Error!! A number can't be divided to 0.")
            print("Exit the program...")
            break
        else:
            print("Result of division: " , a / b)

    else:
        print("1 - 2 - 3 - 4 You can't type without these numbers.")
        print("Exit the program...")
        break