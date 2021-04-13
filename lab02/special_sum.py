def caculate_special_sum(n):
    a=0
    for i in range(1,n+1):
        a+=(i-1)*(i-1)*i
    return a
