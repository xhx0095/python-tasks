def merge(a,b):
    x=[1,2,3]
    y=(1,2,3)
    c=[]
    if type(a)==type(b):
       if type(a)==type(x):
           for i in range(0,len(a)):
               c.append(a[i])
           for j in range(0,len(b)):
               c.append(b[j])   
           return c
       elif type(a)==type(y):
               d=a+b
       return d
    else:
        return "false"
