def factorial_trailing_zero(array):                                                                              #1
    """ This function returns the trailing
        number of zeros of a factorial number"""

    multiple = 1                                                                                                 #1                 
    five=0                                                                                                       #1

    for i in range(array):                                                                                       #n                                                                                    
        multiple=multiple*(i+1)                                                                                  #n

        for j in range(2,array+1):                                                                               #n

            while j>0:                                                                                           #n
                if j %5==0:                                                                                      #n
                    five= five+1
                    j=j/5                                                                                        #n
                else:
                    break
        return five                                                                                              #1

userInput=int(input("Please enter a number which will return the trailing number of zeros of a factorial: "))    #1
print(factorial_trailing_zero(userInput))                                                                        #1
#total=6n+6
#this algorithm has a big O() of n
