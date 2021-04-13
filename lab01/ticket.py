def get_nearest_lucky_ticket(a):
    k=str(a)
    k1=k
    k2=k
    a=1
    b=2
    c=1
    d=2
    while a!=b:
          a=0
          b=0
          for i in range(0,len(k)):
             if (i % 2) == 0:
               a+=int(k1[i])
             if (i % 2) == 1:
               b+=int(k1[i])
          if a!=b:
            k1=str(int(k1)+1)
    while c!=d:
          c=0
          d=0
          for i in range(0,len(k)):
              if (i % 2) == 0:
                  c+=int(k2[i])
              if (i % 2) == 1:
                  d+=int(k2[i])
              if c!=d:
                  k2=str(int(k2)-1)
    e=int(k1)-int(k)
    f=int(k)-int(k2)
    if e>f:
      print(k2)
    if(e<f):
      print(k1)
    if e==f:
      print(k1,k2)
