
def bruteMPC(list) :
    maximum=0
    c1=0
    c2=0
    endpt=len(list)
    for i in range(endpt) :
        prod_acc=list[i]
        for j in range(i+1,endpt) :
            if maximum<= prod_acc :
               maximum=prod_acc 
               c1=i
               c2=j-1 
            prod_acc*=list[j]
        
        if maximum<= prod_acc :
               maximum=prod_acc
               c1=i
               c2=j 
    return maximum,c1,c2+1

def dNcMPC2(list) :
    endpt=len(list)
    if endpt==1 :
        return list[0],0,1
    else :
      lh=list[0:endpt/2]
      print lh
      rh=list[endpt/2:endpt]
      print rh
      left,i1,i2=dNcMPC2(lh)
      print "leftside : ", left,i1,i2
      b0=left==lh[i1:i2]
      print "Interval_left calculation correct?", b0  
      right,j1,j2=dNcMPC2(rh)
      b1 = right == rh[j1:j2]
      print "Interval_right calculation correct?", b0  
      right,j1,j2=dNcMPC2(rh)
      j1,j2=j1+endpt/2,j2+endpt/2
      print "rightside : ", right,j1,j2
      if j1 == i2   :
         if left>=1 and right>=1 :
            return left*right,i1,j2
         else :
            maximum=max(left,right)
            if(maximum == left ) :
               return maximum,i1,i2
            else :
               return maximum,j1,j2
      else :
         midl=list[i2:j1]
         acc=prod(midl)
         print "middle" ,midl
         maximum=max(left,right,left*acc*right)
         if maximum == left*acc*right :
            return maximum, i1, j2
         if acc < 1 :
             ml,itr1 = breakup_left(midl)
             mr,itr2 = breakup_right(midl)
             if(ml*left > mr*right) :
                  return ml*left, i1, i2+itr1
             else :
                  return mr*right,j1-itr2,j2
         else :
             maximum=max(left,right,acc)
             if maximum==left :
                return maximum, i1, i2
             elif maximum == acc :
                return maximum,i2,j1
             else :
                return maximum,j1,j2   
             
def breakup_left(list) :
    endpt = len(list)
    tmp = 1
    cnt=0
    for i in range(endpt) :
        if tmp <= tmp*list[i] :
           tmp*=list[i]
           cnt=i
        else :
           break
    if list == [] :
        return tmp,cnt
    else :
        return tmp,cnt+1

 
def breakup_right(list) :
    endpt = len(list)
    tmp = 1
    cnt=0
    for i in range(endpt) :
        if tmp <= tmp*list[endpt-1-i] :
           tmp*=list[endpt-1-i]
           cnt=i
        else :
           break
    if list == [] :
        return tmp,cnt
    else :
        return tmp,cnt+1


def dNcMPC(list) : 
    endpt=len(list)
    if endpt==1 :
        return list[0],0,0
    else :
      lh=list[0:endpt/2]
      rh=list[endpt/2:endpt]
      left,i1,i2=dNcMPC(lh)
      right,j1,j2=dNcMPC(rh)
      j1,j2=j1+endpt/2,j2+endpt/2
      print "left", lh
      print "right", rh
      print "leftside : ", left,i1,i2
      print "rightside", right,j1,j2
      if j1 - i2 == 1 :
         if left>=1 and right>=1 :
            return left*right,i1,j2
         else :
            maximum=max(left,right)
            if(maximum == left ) :
               return maximum,i1,i2
            else :
               return maximum,j1,j2
      else :
         midl=list[i2+1:j1]
         m,mi,mj=dNcMPC(midl)
         mi=mi+i2+1
         mj=mj+i2+1
         print "middle", midl, "prod", m, mi, mj
         maximum=max(left,right)
         if mi==i2+1 and mj==j1-1 :
            return left*m*right,i1,j2 
         elif mj<j1-1 and mi==i2+1 :
            return left*m,i1,mj
         elif mi>i2+1 and mj==j1-1 :
            return right*m, mi,j2
         elif maximum == left :
            return maximum, i1, i2
         else :
            return maximum, j1, j2


def prod(list) :
    p=1
    for i in range(len(list)) :
       p*=list[i]
    return p

def dpMPC(list) :
    z=1
    acclist=[0]*len(list)
    for i in range(len(list)) :
       z*=list[i]
       acclist[i]=z
    return acclist


def bruteAPC(list) :
    maximum=0
    endpt=len(list)
    for i in range(len(list)-1) :
        prod_acc=list[i]
        for j in range(i+1,endpt) :
            maximum=max(maximum,prod_acc)
            print maximum,prod_acc
            prod_acc+=list[j]
        maximum=max(maximum,prod_acc)
    return maximum

def dNcAPC(list) :
    endpt=len(list)
    if endpt==1 :
        return list[0],0,0
    else :
      lh=list[0:endpt/2]
      rh=list[endpt/2:endpt]
      left,i1,i2=dNcAPC(lh)
      right,j1,j2=dNcAPC(rh)
      j1,j2=j1+endpt/2,j2+endpt/2
      midl=list[i2+1:j1]
      acc=sum(midl)
      maximum=max(left,right,left+acc+right)
      if maximum == left+acc+right :
          return maximum, i1, j2
      elif maximum == left :
           if acc < 0 :
                return maximum, i1, i2
           else :
                return maximum+acc, i1, j1-1
      else :  
               if acc < 0 :
                  return maximum, j1, j2
               else :
                  return maximum+acc, i2+1, j2

   
def check(list) :
    m,i,j=dNcMPC(list)
    chk_m,chk_i,chk_j=bruteMPC(list)
    m2,i2,j2=dNcMPC2(list)
    z1=prod(list[i:j])
    z2=prod(list[i2:j2])
    z3=prod(list[chk_i:chk_j])
    if z3==chk_m :
        print "Brute Force Correct!" , chk_m,chk_i,chk_j
    else :
         print "Brute Fail" 
    if z2==m :
        print "divConq2 Correct" , m2,i2,j2
    else :
        print "divConq2 fails"    
    if z1==m :
        print "divConq Correct!" , m,i,j
    else :
        print "divConq fails!"
    






