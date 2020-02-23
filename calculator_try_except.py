'''
Write a calculator program using try except blocks
'''
print("""
1-addition
2-subtraction
3-multiple
4-devide
""")


while True:
    count = input("choose a process: ")
    first = input("First Number (q for exit): ")
    second = input("Second Number: ")
    if first == "q": break
    if count == "1":
        try:
            number1 = int(first)
            number2 = int(second)
            print(number1, "+", number2, "=", number1 + number2)
        except (ValueError):
            print("ERROR!!!")
            print("Do not enter a word!!!")
        continue
    elif count == "2":
        try:
            number1 = int(first)
            number2 = int(second)
            print(number1, "-", number2, "=", number1 - number2)
        except (ValueError):
            print("ERROR!!!")
            print("Do not enter a word!!!")
        continue
    elif count == "3":
        try:
            number1 = int(first)
            number2 = int(second)
            print(number1, "*", number2, "=", number1 * number2)
        except (ValueError):
            print("ERROR!!!")
            print("Do not enter a word!!!")
        continue
    else :
        try:
            number1 = int(first)
            number2 = int(second)
            print(number1, "/", number2, "=", number1 / number2)
        except (ValueError, ZeroDivisionError):
            print("ERROR!!!")
            print("Do not enter a word or do not enter 0 !!!")
        continue
