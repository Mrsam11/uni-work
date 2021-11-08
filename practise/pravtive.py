'''# Python Program to check character is Alphabet Digit or Special Character
ch = input("Please Enter Your Own Character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print("The Given Character ", ch, "is an Alphabet") 
elif(ch >= '0' and ch <= '9'):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is a Special Character")'''
x = input("Enter ")
if (x.isdigit()):
    print("It is Digit")
elif (x.isalpha()):
    print("it is Alpha")
else:
    print("It is Symbol")