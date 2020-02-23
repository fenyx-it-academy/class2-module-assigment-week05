#print out the options you have
print("Welcome to calculator")
i=1
while i==1:  #We set while loop for ask choices again.
    print("1)Addition 2)Subtraction 3)Multiplication 4)Division 5)Quit calculator")
    choice = input("choose your option: ")   #print out the options you have
    try:        #We use try-except for ZeroDivisionError and ValueError in while loop
        if choice=='1':
            add1=int(input("first number:")) #We write all condition:Addition,Subtraction,Multiplication,Division,
            add2=int(input("second number:")) #Quit calculator conditions  in try.
            print(add1,"+",add2,"=",add1+add2)
        elif choice=='2':
            sub1=int(input("first number:"))
            sub2=int(input("second number:"))
            print(sub1,"-",sub2,"=",sub1-sub2)
        elif choice=='3':
            mul1=int(input("first number:"))
            mul2=int(input("second number:"))
            print(mul1,"x",mul2,"=",mul1*mul2)
        elif choice=='4':
            div1=int(input("first number:"))
            div2=int(input("second number:"))
            print(div1,"/",div2,"=",div1/div2)
        elif choice == '5':
            i=0
            print("Thank you for using calculator")
        else:
            print("Please enter 1,2,3,4,5 numbers.It is not valid input")

    except ZeroDivisionError:        # If there is ZeroDivisionError or ValueError, we write exception
        print("Cannot divide by zero!You should be careful!!!!!")
    except ValueError:
        print("Please enter numbers.It is not number")
