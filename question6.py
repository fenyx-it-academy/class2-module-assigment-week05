def add(x,y):# This function adds two numbers
    return x+y
def subtract(x,y):# This function subtracts two numbers
    return x-y
def multibly(x,y):# This function multiplies two numbers
    return x*y
def divide(x,y):# This function divides two numbers
    return x/y

print("Welcome Calculator!")
print("""****************
Select operation;
1.Add
2.Subtract
3.Multiply
4.Divide
5.Quit
*********************""")
while True:
    try:#we used the try blog to catch errors
        choice=input("Enter choice(1/2/3/4/5):")# Take input from the user
        if choice=='5':#Since we do not enter as choice integer, we get these as string
            print("You Quit!")
            break

        number1 = float(input("enter first number:"))
        number2 = float(input("enter second number:"))

        if choice=='1':
            print(number1,"+",number2,"=",add(number1,number2))

        elif choice == '2':
            print(number1,"-",number2,"=",subtract(number1,number2))

        elif choice == '3':
            print(number1, "*", number2, "=", multiply(number1, number2))

        elif choice == '4':
            try:#we used the try blog to prevent the user from error and to produce a more understandable message
               print(number1, "/", number2, "=", divide(number1, number2))
            except ZeroDivisionError:#this warning will be given in case of 0 in the section
                print("Can not divide by Zero!")

        else:#This warning will come when a number other than 1,2,3,4,5 is entered.
            print("invalid input!")

    except ValueError:
        #The error that will be generated if the user enters inappropriate data during the data conversion process is a ValueError.
        # So the name of the error type we will write in the except block is ValueError.
        print("Please enter only numbers!")
