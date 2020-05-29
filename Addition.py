# Improve your Addition !

# Enter the First input of number which is inclusive
# Enter the Second input of number which is excusive

# And Enjoy !


import numpy as np # imports NumPy library, if you haven't installed please check numpy.org

def Addition(): # Defines a function
    a = int(input("Please enter the First Number : ")) # Asks for input and assigns to variable a
    b = int(input("Please enter the Second Number : ")) # Asks for input and assigns to variable b
    
    x = np.random.randint(a, b) # Generates a random number and assigns to variable x
    y = np.random.randint(a, b) # Generates a random number and assigns to variable y
    
    print(x,"+",y) # Prints x + y
    
    f = input() # Asks for input and assigns to f
    
    while int(f) == x+y: # Compares the input with x+y
        x = np.random.randint(a,b) # Generates a random number and assigns to variable x
        y = np.random.randint(a,b) # Generates a random number and assigns to variable y
        print(x,"+",y) # Prints x + y
        f = input() # Asks for input and assigns to f
        
    else: # If the above condions fails, this runs
        print(x,"+",y,"=", x+y) # Prints x + y and value of x + y
        choice = input("Do You want to start again ! Yes or No, Please :") # Asks if want to continue or not
        if choice.lower() == "yes": # Matches the input
            Addition() # Runs the module
        elif choice.lower() == "no": # Matches the input
            print("Thanks for playing !") # Prints message
        else: # If the Above conditions fails, this runs
             print("See You again in future !") # Prints the message
Addition() # Runs the main module for the first time
