num = 7 #for factorial from 1 to 7
sum = 0
print('The Sum of Factorial ')
for i in range(num,0,-1):
    fact = 1
    for j in range(i,0,-1):
        fact = fact * j
    sum += fact
    print(str(i)+ '!' , end=" ")
print('is',sum)
s = 0 #for sum of numbers from 1 to 7
for j in range(1,8):
    s = s +j
print('The Sum of Numbers from 1 to 7 is ' ,s)
#for the sum of series along with their factorial till 7th
print('The Sum of series along with their factorial till 7 is ', s/sum)