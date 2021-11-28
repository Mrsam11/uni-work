n = int(input('Enter number to check its armstrong or not '))
sum = 0
n2 = n
order = len(str(n))
while(n>0):
    digit = n%10
    print(f'digit is {digit}')
    sum += digit**order
    n = n//10
if sum==n2:
    print(f'{n2} is an armstrong number')
else:
    print(f'{n2}  is not an armstorng number')