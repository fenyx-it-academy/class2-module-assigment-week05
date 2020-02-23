import time

def calc_choice():  # We define a function for user enter input and select the calculation method from the menu.
    print('''
    Sum = 1
    Subtraction = 2
    Multiplication  = 3
    Division  = 4
    Power  = 5
    Exit   = 6
    ''')
    while True:
        choice = input('Please enter a number between 1-6 to make a choice: ')
        if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6':
            print('Please proceed for calculation.')
            time.sleep(1)
            return choice  # The output of this function is the method choice of the user.


def calculator():  # We define a function to make calculations.
    while True:
        num1 = input('Please enter the first number: ')  # We get 2 numbers as an input from the user.
        num2 = input('Please enter the second number: ')
        try:  # If the numbers are entered correctly, the calculation will be made based on user's choice.
            num1 = int(num1)
            num2 = int(num2)
            choice = calc_choice()  # We use the function for user's choice here to initiate the demanded method.
            if choice == '1':
                return num1+num2
            elif choice == '2':
                return num1-num2
            elif choice == '3':
                return num1*num2
            elif choice == '4':
                try:  # If the divisor is 0, we warn the user to reenter the values.
                    return num1/num2
                except ZeroDivisionError:
                    print('Divisor cannot be zero.')
                    continue
            elif choice == '5':
                return num1**num2
            elif choice == '6':
                return 'You have exited the calculator.'
        except ValueError:  # If the numbers are not valid, we warn the user.
            print('Please enter valid numbers for calculation or enter q to exit.')
            continue


print(calculator())
