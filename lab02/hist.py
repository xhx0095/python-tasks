def distribute(a,k):
    x=min(a)
    y=max(a)
    b=abs((y-x)/k)
    c=[]
    d=sorted(a)
    z=[0]*k
    m=0
    j=0
    while m<=k-1 and j<=len(d)-1:
          if x+(m*b)<=d[j]<x+((m+1)*b):
              z[m]=z[m]+1
              j=j+1
          else:
              m=m+1
    z[k-1]=z[k-1]+1
    return z
