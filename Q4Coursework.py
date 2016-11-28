import random

array=[1,2,3,4,5,6,7,8,9,10]                                       #1

def randomShuffle(array):                                          #1
    """ This function shuffles numbers randomly and it
    it is based on the knuth shuffle"""

    countNumbers=len(array)                                        #1
    
    #looking through the array starting from the last element
    for i in range(countNumbers-1,0,-1):                           #n                       
        
        #Generates random number
        j=random.randint(0,countNumbers-1)                         #n

        #swaps the numbers arounds
        temp= array[i]                                             #n
        array[i]=array[j]                                          #n
        array[j]=temp                                              #n

    return array                                                   #1

print(randomShuffle(array))                                        #1
#total=5n+5
#this algorithm has a big O() of n
