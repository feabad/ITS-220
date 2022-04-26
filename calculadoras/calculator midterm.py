def Menu():
    print ("""+-*/=+-*/=+-*/=
Calculator
+-*/=+-*/=+-*/=
Menu
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Quit""")
def Calculator():
    Menu()
    operation = int(input("Enter your option:\n"))
    while (operation >0 and operation <5):
        x = float(input("Enter your first number:\n"))
        y = float(input("Enter your second number:\n"))
        if (operation==1):
            print ("Result:", x+y)
            operation = int(input("Enter your option:\n"))
        elif(operation==2):
            print ("Result:",x-y)
            operation = int(input("Enter your option:\n"))
        elif(operation==3):
            print ("Result:",x*y)
            operation = int(input("Enter your option\n"))
        elif(operation==4):
            try:
              print ("Result:", x/y)
              operation = int(input("Enter your option\n"))
            except ZeroDivisionError:
              print ("Division by zero is not allowed!")
              operation = int(input("Enter your option\n"))
Calculator()
