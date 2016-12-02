##Pseudocode
## binarySearch(array,left,right)
## left<-0
## right<- COUNT array-1
## WHILE TRUE
##     IF left>right
##         RETURN NULL
##     m<- (left+right)/2
##     IF array[m] <left
##        left<-m+1
##     IF array[m]>right
##        right<-m-1
##     IF array[m]>= left AND array[m]<= right
##        RETURN M
## array=INPUT "Enter a list of numbers in accending order which is seperated by commas:"
## commas<- array.SPLIT ","
##userInput1<- INPUT "Enter the leftside of number for which to be found: "
##userInput2<- INPUT "Enter the rightside of number for which to be found: "
##PRINT "The range of "userInput1 +" and " userInput2+ " is " binarySearch(array,userInput1,userInput2)
def binarySearch(array,left,right):                                                                                         #1
    left= 0                                                                                                                 #1
    
    right=int(len(array)-1)                                                                                                 #n
    while True:                                                                                                             #n
        if int(left)>right:                                                                                                 #1
            return None
        m=int((left+right)//2)                                                                                              #n                                                                            
        if int(array[m])<left:
            #checks left side of the array
            left=m+1                                                                                                        #n                                                               
        if int(array[m])>right:                                                                                             #n
            #checks right side of the array
            right=m-1                                                                                                       #n
        if int(array[m])>= left and int(array[m])<= right:                                                                  #n
            #checks between both sides of the array
            return m                                                                                                        #1
array=input("Enter a list of numbers in accending order which is seperated by commas: ")                                    #1
commas= array.split(",")                                                                                                    #1
userInput1=int(input("Enter the leftside of number for which to be found: "))                                               #1
userInput2=int(input("Enter the rightside of number for which to be found: "))                                              #1

print("The range of "+str(userInput1)+" and " +str(userInput2)+ " is "+str( binarySearch(array,userInput1,userInput2)))     #1
#BigO=9+7n
#The Big O notation of this code is n
            






