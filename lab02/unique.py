def compress(a):
    b=list(set(a))
    c=[0]*len(b)
    d=[0]*len(b)
    for i in range(0,len(b)):
        for item in a:
            if b[i]==item:
                c[i]+=1
    for i in range(0,len(b)):
        d[i]=(b[i],c[i])
    return d
