import random

array=[1,2,3,4,5,6,7,8,9,10]

def randomShuffle(array):
    """ This function shuffles numbers randomly and it
    it is based on the knuth shuffle"""

    countNumbers=len(array)
    
    #looking through the array starting from the last element
    for i in range(countNumbers-1,0,-1):                          
        
        #Generates random number
        j=random.randint(0,countNumbers-1)

        #swaps the numbers arounds
        temp= array[i]
        array[i]=array[j]
        array[j]=temp

    return array

print(randomShuffle(array))
