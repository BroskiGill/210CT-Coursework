def binarySearch(array,left,right):
    left= 0
    
    right=int(len(array)-1)
    while True:
        if int(left)>right:
            return None
        m=int((left+right)//2)
        if int(array[m])<left:
            left=m+1
        if int(array[m])>right:
            right=m-1
        if int(array[m])>= left and int(array[m])<= right:
            return m
array=input("Enter a list of numbers in accending order which is seperated by commas: ")
commas= array.split(",")
userInput1=int(input("Enter the leftside of number for which to be found: "))
userInput2=int(input("Enter the rightside of number for which to be found: "))

print("The range of "+str(userInput1)+" and " +str(userInput2)+ " is "+str( binarySearch(array,userInput1,userInput2)))
            






