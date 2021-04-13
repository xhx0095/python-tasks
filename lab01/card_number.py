def check_card_number(a):
      c=[]
      f=[]
      while a!=0:
            b=a%10
            c.append(b)
            a=int(a/10)
      e=c
      for i in range(0,len(e)):
          if i%2!=0:
              if (e[i]*2)<10:
                  e[i]=e[i]*2
              else:
                  h=e[i]*2
                  while h!=0:
                       g=h%10
                       f.append(g)
                       h=int(h/10)
                  e[i]=sum(f)
      x=sum(e)
      if x%10==0:
          return "true"
      else:
          return "false"
def  check_card_number_str(a):
       b=[]
       f=[]
       for j in range(0,len(a)):
            b.append(int(a[j]))             
       e=list(reversed(b))
       for i in range(0,len(e)):
          if i%2!=0:
              if (e[i]*2)<10:
                  e[i]=e[i]*2
              else:
                  h=e[i]*2
                  while h!=0:
                       g=h%10
                       f.append(g)
                       h=int(h/10)
                  e[i]=sum(f)
       x=sum(e)
       if x%10==0:
          return "true"
       else:
          return "false"
def gen_card_num(start, total_num):
    a = start
    while len(a) < total_num - 1:
        result += str(random.randint(0, 9))
    s = 0
    card_num_length = len(result)
    for _ in range(2, card_num_length + 2):
        t = int(result[card_num_length - _ + 1])
        if _ % 2 == 0:
            t *= 2
            s += t if t < 10 else t % 10 + t // 10
        else:
            s += t
    t = 10 - s % 10
    a += str(0 if t == 10 else t)
    return a
