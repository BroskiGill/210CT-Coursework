b=[[1,5,3,2],
   [6,8,2,1],
   [7,1,3,7]]

c=[[8,2,4,2],
   [6,3,2,4],
   [7,1,6,3]]

def matrixAdd(b,c):
    r=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]

    #Going through the rows
    for i in range(len(b)):

    #Going through the columns

        for j in range(len(b[0])):
            r[i][j]=b[i][j]+c[i][j]
    return r

def matrixSub(b,c):
    r=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
    for i in range(len(b)):
        for j in range(len(b[0])):
            r[i][j]=b[i][j]-c[i][j]
    return r

def matrixMulti(b,c):
    r=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
    for i in range(len(b)):
        for j in range(len(b[0])):
            r[i][j]=b[i][j]*c[i][j]
    return r



x=matrixMulti(b,c)
y=matrixAdd(b,c)
a=matrixSub(x)

print(a)
    
