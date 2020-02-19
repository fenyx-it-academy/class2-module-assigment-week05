"""
Write a calculator program using try except blocks

"""

def welcome_func():
    """ This function say Welcome to user and invoke operation_func() which take input for operator  """

    print('Welcome to Calculator')
    operation_func()

def operation_func():
    """ This function take input from user to choose math operator.
        if user cant enter correct type of math operator, the function will be called again  """

    operation_input = input("\nPlease type in the math operation you would like to complete:\n+ for addition\n- for subtraction\n* for multiplication\n/ for division : ")
    operation_list = ["+", "-", "*", "/"]
    if not operation_input in operation_list: 
        print('\nYou have not typed a valid operator!!! \nPlease enter the math operation again.')
        operation_func()

    return calculate_func(operation_input)

def calculate_func(operation):
    """ This function take input numbers from user to calculate.
        if user enter string or float instead of int, ValueError will be printed 
        if user enter zero the second number for division, ZeroDivisionError will be printed """

    try:
        number_1 = int(input('\nPlease enter the first number: '))
        number_2 = int(input('Please enter the second number: '))
        if operation == '+':
            result = number_1 + number_2
            print('{} + {} = {} '.format(number_1, number_2, result))
        elif operation == '-':
            result = number_1 - number_2
            print('{} - {} = {} '.format(number_1, number_2, result))
        elif operation == '*':
            result = number_1 * number_2
            print('{} * {} = {} '.format(number_1, number_2, result))
        elif operation == '/':
            try:
                result = number_1 / number_2
                print('{} / {} = {} '.format(number_1, number_2, result))
            except ZeroDivisionError:
                print("Second number can not be zero…")

        again_func()
    except ValueError:
        print("Warning! Please enter a number..")
        calculate_func(operation)
    

def again_func():
    """ This function ask user if calculate numbers again """
    calc_again = input("\nDo you want to calculate again?\nPlease enter Y for YES or N for NO : ")
    if calc_again.upper() == 'Y':
        operation_func()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again_func()

welcome_func()

# THE END