fact = 1
sum=0
for i in range(1,8):
    for j in range(i,0,-1):
        fact= fact *j # calculating factorial
    div = i/fact # divide num with their factorial
    sum = sum + div # calculating sum 
print("\nSum of First Seven Terms : ",sum)
    