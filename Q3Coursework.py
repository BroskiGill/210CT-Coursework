def highest_Perfect_Square(n):
    """ This function will return the highest perfect
        square of number that is given"""
    x=n
    
    while True:
        #Calculates the perfect square
        if x**2<=n:
            return("The number "+str(n) +" closest perfect square is "+str((x**2)))

        #returns back to functions
        
        else:
            x=x-1

userInput=int(input("Please enter a number for which will return the closest perfect square: "))
print(highest_Perfect_Square(userInput))

