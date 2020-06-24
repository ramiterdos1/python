from random import randrange

def randMatrix(inp) :
    r=[]
    for i in range(inp) :
      r.append([(-1)**(randrange(57+i)%2) for i in range(inp)])
    return r

def printRandMat(r) :
    for i in r :
       for j in i:
           print j,
       print '\n'



