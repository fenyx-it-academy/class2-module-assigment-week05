total=0

def add(num):
    global total
    total += num
    return total

def subtract(num):
    global total
    total -= num
    return total

def multiply(num):
    global total
    total *= num
    return total

def divide(num):
    global total
    total /= num
    return total

while True:
    try:
        first_num=float(input("Enter a number"))
        total += first_num
        break

    except ValueError:
        print("Just number!")

#ikinci döngü ilk numaranın üzerine ekleyerek devam edecek. ilk numarayı ikinci döngünün içinde alsaydım
# örn: 5 + 10 işleminden sonra 15 yazdırıp ikinci döngüye geçince tekrar sayı istiyordu, sıradaki işlemi değil.
while True:
    try:
        operation = input("+,-,*,/,=")

        if operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "=":
            print("Faulty Input!")
            print(total)
            continue

        if operation == "=":
            print("Result --->" ,total)
            break

        num=float(input("Enter a number:"))

        if operation == "+":
            print(add(num))

        elif operation == "-":
            print(subtract(num))

        elif operation == "*":
            print(multiply(num))

        elif operation == "/":
            print(divide(num))

    except ValueError:
        print("Just number!")
        print(total)

    except ZeroDivisionError:
        print("Numbers cannot be divided by zero.")
        print(total)