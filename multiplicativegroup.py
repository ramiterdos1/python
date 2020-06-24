import numpy as np

def table(mod) :
     a=np.array([[0]*mod]*mod)
     for i in range(mod) :
        for j in range(mod) :
            a[i][j]= (i*j+1+i+j) % mod
     return a
