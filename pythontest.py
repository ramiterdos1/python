def prime(n):
    result=[2]
    for i in range(3,n,2):
        j=0
        while j<len(result):
            if i%result[j]==0:break
            else j=j+1 
        if j==len(result):
            result.append(i)
    return result;
def powr(m,n):
    if n==0:
        return 1;
    else:
        if n%2==0:
            z=powr(m,n/2);
            return z*z;
        else:
            z=powr(m,(n-1)/2);
            return m*z*z;
        
