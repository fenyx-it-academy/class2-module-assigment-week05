def caculator(x, y):
    try:
        print(f'{x}/{y}: {x / y}')
    except ZeroDivisionError:
        print("division by zero!")
    try:
        print(f'{x}+{y}: {x + y}')
    except:
        print("Something went wrong add")
    try:
        print(f'{x}-{y}: {x - y}')
    except:
        print("Something went wrong substract")
    try:
        print(f'{x}*{y}: {x * y}')
    except:
        print("Something went wrong multiply")
    finally:
        print("executing finally clause")


caculator(3, 0)

