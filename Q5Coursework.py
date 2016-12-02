#Pseudocode
##b<-[[1,5,3,2],
##   [6,8,2,1],
##   [7,1,3,7]]
## c<-[[8,2,4,2],
##    [6,8,2,1]
##    [7,1,3,7]]
##

## matrixAdd(b,C)
## r<-[[0,0,0,0],
##     [0,0,0,0],
##     [0,0,0,0]]
##COMMENT  going through rows
## for i in from COUNT b
##COMMENT   going through columns
##     for j in from COUNT b[0]
##          r<-r[i][j]=b[i][j]+c[i][j]
## return r

## matrixSub(b,C)
## r<-[[0,0,0,0],
##     [0,0,0,0],
##     [0,0,0,0]]
## for i in from COUNT b
##     for j in from COUNT b[0]
##          r<-r[i][j]=b[i][j]-c[i][j]
## return r

## matrixMulti(b,C)
## r<-[[0,0,0,0],
##     [0,0,0,0],
##     [0,0,0,0]]
## for i in from COUNT b
##     for j in from COUNT b[0]
##          r<-r[i][j]=b[i][j]*c[i][j]
## return r
##e<-matrixMulti(b,c)
##f<-matrixAdd(b,c)
##a<-matrixSub(e)
## PRINT a

