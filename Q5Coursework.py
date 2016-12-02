#Pseudocode
##b<-[[1,5,3,2],                                                                     #1
##   [6,8,2,1],                                                                      #1
##   [7,1,3,7]]                                                                      #1
##
## c<-[[8,2,4,2],                                                                    #1
##    [6,8,2,1]                                                                      #1
##    [7,1,3,7]]                                                                     #1
##

## matrixAdd(b,C)                                                                    #1
## r<-[[0,0,0,0],                                                                    #1
##     [0,0,0,0],                                                                    #1
##     [0,0,0,0]]                                                                    #1
##COMMENT  going through rows
## for i in from COUNT b                                                             #n
##COMMENT   going through columns
##     for j in from COUNT b[0]                                                      #n
##          r<-r[i][j]=b[i][j]+c[i][j]                                               #n^2
## return r                                                                          #1

## matrixSub(b,c)                                                                    #1
## r<-[[0,0,0,0],                                                                    #1
##     [0,0,0,0],                                                                    #1
##     [0,0,0,0]]                                                                    #1
##COMMENT  going through rows
## for i in from COUNT b                                                             #n
##COMMENT   going through columns
##     for j in from COUNT b[0]                                                      #n
##          r<-r[i][j]=b[i][j]-c[i][j]                                               #n^2
## return r                                                                          #1

## matrixMulti(b,c)                                                                  #1
## r<-[[0,0,0,0],                                                                    #1
##     [0,0,0,0],                                                                    #1
##     [0,0,0,0]]                                                                    #1
##COMMENT  going through rows
## for i in from COUNT b                                                             #n
##COMMENT   going through columns
##     for j in from COUNT b[0]                                                      #n
##          r<-r[i][j]=b[i][j]*c[i][j]                                               #n^2
## return r                                                                          #1
##
##e<-matrixMulti(b,c)                                                                #1
##f<-matrixAdd(b,c)                                                                  #1
##a<-matrixSub(e)                                                                    #1               
## PRINT a                                                                           #1
## bigOtotal<- 25+6n+3n^2
## The big O notation of this is 

