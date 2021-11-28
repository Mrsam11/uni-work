dic ={}
leng = 'y'
while leng=='y':
    key = input('Enter Your Name ')
    value = input('Enter Number ')
    dic[key] = value
    leng = input('If you want to add More numbers in phone book press Y else N :').lower()
    if leng =='n':
        break
print(dic)