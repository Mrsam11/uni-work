#Pyton program to convert height (in feet and inches) to centimeter
#1 feet = 12 inches
feet = 5
inches = 12
con_inches = feet * inches
print("5 feets to inches :", end=" ") 
print(con_inches, "inches")
#add 2 inche
Inch = 2
add_inch = con_inches + Inch
print("Add Up inches :", end=" ")
print(add_inch, "inches")
#Convert inches to cm
cm = 2.54
con_cm = add_inch * cm
print("convert inches to cm :", end=" ")
print(con_cm, "cm")
'''Python program to compute distance between
two points(Pythagorean Theorem)'''
x1 = 5
x2 = 8
y1 = 12
y2 = 16
#Formula
Distance = ((x2-x1)**2+(y2-y1)**2)**1/2
print("The Distance between two point :", Distance)
#Python program to print students Biodata
name = input("Enter your name ")
dob = input('Enter your Date of Birth ')
roll = input('Enter Your Roll No ')
section = input("Enter your Section ")
mm = input('Enter your Matric Marks ')
mp = input('Enter your Matric Percentage ')
em = input('Enter your Enter Marks ')
ep= input('Enter your Enter Percentage ')
print("Name :", end="\t\t\t")
print(name)
print("Date Of Birth :", end= " \t")
print(dob)
print("Roll No :", end="\t\t")
print(roll)
print("Section :", end="\t\t")
print(section)
print("Matric Marks :", end="  \t")
print(mm)
print("Matric percentage :", end= " \t")
print(mp ,'%')
print("Enter Marks : ", end= "\t\t")
print(em)
print("Enter Percentage : ", end= " \t")
print(ep,'%')
#Python Program for Food Ordering
food= input("What Kind Of Food You Would Like To have ")
print("Let me see if I can find you a" , food.upper())
#Python program for Making Marksheet
#Marks Obtain in courses
#Each course = 50 marks
course1 = int(input ('Enter your Marks in English '))
course2 = int(input ('Enter your Marks in Math '))
course3 = int(input ('Enter your Marks in Physics '))
course4 = int(input ('Enter Your Marks in Chemistry '))
course5 = int(input ('Enter Your Marks in Urdu '))
#Calculate Total Marks
Total_marks= course1+course2+course3+course4+course5
#Calculate average
average = Total_marks/5
#Calculate Percentage
Course_marks = 250
percentage = (Total_marks * 100)/Course_marks
print("Marks you Obtain in English is ", end="")
print(course1)
print("Marks you Obtain in Math is ", end="")
print(course2)
print("Marks You Obtain in Physics is ", end="")
print(course3)
print("Marks you Obtain in Chemistry is ", end="")
print (course4)
print("Marks you Obtain in Urdu is ", end="")
print(course5)
print("Your Total Marks is ", end= "")
print(Total_marks)
print("The total Marks of Course is ", end="")
print(Course_marks)
print("Your Average Marks is ", end="")
print(average)
print("Percentage You Obtain is ", end="")
print(percentage)
