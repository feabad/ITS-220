def Calculator():
    while True:
        oper = input('Enter your option: +, -, *, / or Q to quit ')
        if oper == 'q' or oper == 'Q':
            break
        elif oper == '+' or oper == '-' or oper == '*' or oper == '/':
            num1 = float(input('Enter your first number:  '))
            num2 = float(input('Enter your second number:  '))
        else:
            print('Invalid operation')

        if oper == '+':
            total = num1 + num2
            print(total)
        elif oper == '-':
            total = num1 - num2
            print(total)
        elif oper == '*':
            total = num1 * num2
            print(total)
        elif oper == '/':
            try:
                total = num1 / num2
                print(total)
            except ZeroDivisionError:
                print ("Attention! A number can not be divided by zero.\n")
Calculator()

                  
