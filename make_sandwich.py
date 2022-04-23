def make_sandwich():
    jelly = input("What flavor of jelly would you like? ")
    butter = input("OK - and how about the butter? ")
    print("Thanks. Let's go!")
    print("Stirring the butter...")
    print("Spreading " + jelly + " jelly "+ "onto one slice!")
    print("Now spreading " + butter + " butter "+ "onto the other slice!")
    print("Finished! There's your " + butter + " butter" + " and " + "jelly" + " sandwich!")

print("Welcome to sandwich-matic 2.0")
another = "Y"
while another == "Y":
    make_sandwich()
    another = input("How about another(Y/N)? ")

