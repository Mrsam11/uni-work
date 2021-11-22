lv= 900
uv=1000
for i in range(lv,uv+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
    else:
        print('0 and 1 are not prime')