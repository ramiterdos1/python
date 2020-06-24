def BigramSim(inp,N) :
    f=open(inp,"r")
    lines=[line.split() for line in f]
    words=[]
    for l in lines :
       for w in l :
           words.append(w)

    f.close()
    length=len(words)-1
    bigram=[(words[i],words[i+1]) for i in range(length)]
    bigramfreq=[bigram.count(i) for i in bigram]
    d=dict(list(zip(bigram,bigramfreq)))
    aux=[(d[key],key) for key in d]
    aux.sort()
    aux.reverse()
    return aux[0:N]


