import numpy as np


def main():
    name = input("What is Your Name ? ")
    print("Please input !")
    what = input('"+" for Addition, "-" for Substraction, "x" for Multilication "/" for Division ')

    if what.lower() == "+":
        print()
        print("Hello", name.title())
        print()
        addition()
        
    elif what.lower() == "x":
        print()
        print("Hello", name.title())
        print()
        multiplication()

    elif what.lower() == "-":
        print()
        print("Hello", name.title())
        print()
        substraction()

    elif what.lower() == "/":
        print()
        print("Hello", name.title())
        print()
        division()

    else:
        print()



def addition():
    score =[]
    a = int(input("Please enter the First Number : "))
    b = int(input("Please enter the Second Number : "))
    
    x = np.random.randint(a, b+1)
    y = np.random.randint(a, b+1)

    print()

    print("Please Add the 2 number and input the value")
    print("Hit Enter")
    print("Repeat the above two steps")
    print("Please don't hit enter without any input or the program will terminate")
    print("Enjoy !")

    print()

    def m1():
        while True:
            try:
                print("Highest Score is", score[0])
                break
            
            except LookupError:
                print("Highest Score is 0")
                break
    
    m1()

    print(x,"+",y)
    
    f = input()

    z = []

    if f.lower() == "abort":
        print("Game Aborted")
        main()

    elif f.lower() == "":
        print("You forget to input a value")
        main()

    else:
        while int(f) == x+y:
            x = np.random.randint(a,b+1)
            y = np.random.randint(a,b+1)
            print(x,"+",y)
            f = input()

            if f.lower() == "abort":
                print("Game Aborted")
                main()

            elif f.lower() == "":
                print("You forgot to input a value")
                print("Please enter the input")
                f = input()

            z.append(f)

        else:
            print(x,"+",y, "=", x+y)
            print("Your Score is", len(z))
            print("Please start again !")
            print()
            main()

        
def multiplication():
    a = int(input("Please enter the First Number : "))
    b = int(input("Please enter the Second Number : "))
    
    x = np.random.randint(a, b+1)
    y = np.random.randint(a, b+1)
    
    print(x,"X",y)
    
    f = input()

    z = []
        
    while int(f) == x*y:
        x = np.random.randint(a, b+1)
        y = np.random.randint(a, b+1)
        print(x,"X",y)
        f = input()

        z.append(f)

    else:
        print(x,"X",y, "=", x*y)
        print("Your Score is", len(z))
        print("Please start again !")
        main()


def substraction():
    a = int(input("Please enter the First Number : "))
    b = int(input("Please enter the Second Number : "))
    
    x = np.random.randint(a, b+1)
    y = np.random.randint(a, b+1)
    
    print(x,"-",y)
    
    f = input()

    z = []
        
    while int(f) == x-y:
        x = np.random.randint(a, b+1)
        y = np.random.randint(a, b+1)
        print(x,"-",y)
        f = input()

        z.append(f)

    else:
        print(x,"-",y, "=", x-y)
        print("Your Score is", len(z))
        print("Please start again !")
        main()


def division():
    a = int(input("Please enter the First Number : "))
    b = int(input("Please enter the Second Number : "))
    
    x = np.random.randint(a, b+1)
    y = np.random.randint(a, b+1)
    
    print(x,"/",y)
    
    f = input()

    z = []
        
    while float(f) == x//y:
        x = np.random.randint(a, b+1)
        y = np.random.randint(a, b+1)
        print(x,"/",y)
        f = input()

        z.append(f)

    else:
        print(x,"/",y, "=", x//y)
        print("Your Score is", len(z))
        print("Please start again !")
        main()

        
main()
