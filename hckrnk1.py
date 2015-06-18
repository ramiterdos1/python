cube= lambda a: a**3;
fibcalc= lambda a,b: a+b;
N=input();
N=int(N);

l=list([0,1]);
if N ==1 :
    print(l[0:1]);
elif N == 2 :
    print(l);
elif N > 2 :
    for i in range (2, N) :
        l.append(fibcalc(l[i-1],l[i-2]));
    print (list(map(cube,l)));       
