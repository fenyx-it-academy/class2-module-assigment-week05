def calculate(x, operation, y):
    try:
        if operation == "+":
            return int(x)+int(y)
        elif operation == "-":
            return int(x)-int(y)
        elif operation == "*":
            return int(x)*int(y)
        elif operation == "/":
            return int(x)/int(y)
        elif operation not in ["+","*","/","-"]:
            return "Wrong operation sign."
    except ValueError:
        return "Enter a only number!!"
    except ZeroDivisionError:
        return "You can't do every operation that you want!! =)"


print(calculate(x=input(), operation=input(), y=input()))
