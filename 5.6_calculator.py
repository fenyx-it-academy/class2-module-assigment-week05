print("Select operation. 1-(Add) 2-(Subtract) 3-(Multiply) 4-(Divide)")
operation = input('Your selection is(1-2-3-4): ')


def calculator(x, y):

    try:
        if operation == '1':
            return int(x)+int(y)
        elif operation == '2':
            return int(x)-int(y)
        elif operation == '3':
            return int(x)*int(y)
        elif operation == '4':
            return int(x)/int(y)
    except ZeroDivisionError:
        return 'Divider must not be 0!'
    except ValueError:
        return 'You must not leave it blank!'
    except TypeError:
        return 'Only numbers can be operated!'


print(calculator(input('First number: '), input('Second number: ')))
