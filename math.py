import numpy as np



def main():
    what = input('"+" for Addition, "-" for Substraction, "x" for Multilication "/" for Division ')

    if what.lower() == "+":
        addition()
        
    elif what.lower() == "x":
        multiplication()

    elif what.lower() == "-":
        substraction()

    elif what.lower() == "/":
        division()

    else:
        print()


def addition():
    a = int(input("Please enter the First Number : "))
    b = int(input("Please enter the Second Number : "))
    
    x = np.random.randint(a, b)
    y = np.random.randint(a, b)
    
    print(x,"+",y)
    
    f = input()
        
    while int(f) == x+y:
        x = np.random.randint(a,b)
        y = np.random.randint(a,b)
        print(x,"+",y)
        f = input()

    else:
        print(x,"+",y, "=", x+y)
        print("Please start again !")
        main()

        
def multiplication():
    a = int(input("Please enter the First Number : "))
    b = int(input("Please enter the Second Number : "))
    
    x = np.random.randint(a, b)
    y = np.random.randint(a, b)
    
    print(x,"X",y)
    
    f = input()
        
    while int(f) == x*y:
        x = np.random.randint(a,b)
        y = np.random.randint(a,b)
        print(x,"X",y)
        f = input()

    else:
        print(x,"X",y, "=", x*y)
        print("Please start again !")
        main()

def substraction():
    a = int(input("Please enter the First Number : "))
    b = int(input("Please enter the Second Number : "))
    
    x = np.random.randint(a, b)
    y = np.random.randint(a, b)
    
    print(x,"-",y)
    
    f = input()
        
    while int(f) == x-y:
        x = np.random.randint(a,b)
        y = np.random.randint(a,b)
        print(x,"-",y)
        f = input()

    else:
        print(x,"-",y, "=", x-y)
        print("Please start again !")
        main()

def division():
    a = int(input("Please enter the First Number : "))
    b = int(input("Please enter the Second Number : "))
    
    x = np.random.randint(a, b)
    y = np.random.randint(a, b)
    
    print(x,"/",y)
    
    f = input()
        
    while float(f) == x//y:
        x = np.random.randint(a,b)
        y = np.random.randint(a,b)
        print(x,"/",y)
        f = input()

    else:
        print(x,"/",y, "=", x//y)
        print("Please start again !")
        main()


        
main()
