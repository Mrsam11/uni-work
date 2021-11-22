def gcd(a,b):
    if a == 0 :
        mn = b
    elif b == 0:
        mn = a
    elif b>a :
        mn = a
    else:
        mn = b
    for i in range(1,mn+1):
        if a%i==0 and b%i==0:
            hcf = i
    print(hcf)
    
gcd(0,0)
    