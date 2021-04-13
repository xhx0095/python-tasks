import itertools
def transpose(a):
    b = zip(* a)
    b = list(b)
    return b

def scalar_product(a,b):
    try:
        a1=map(lambda x,y:int(x)*int(y),a,b)
        a2=sum(list(a1))
        return a2
    except Valueerror:
        return None
