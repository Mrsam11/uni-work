"""python code to demonstrate the working of
polar and rect"""
# importing cmath for complex number
import cmath
import math
# initailizing real numbers
x = 1.0
y = 1.0
# to convert them into complex number
z = complex(x,y)
#convert Complex number to polar
w = cmath.polar(z)
#print modulus and argument of polar complex number
print("The Modulus And Argument - Polar complex number:"
      , end="")
print (w)
# convert complex number into rectanguler using rect()
w = cmath.rect(1.4142135623730951, 0.7853981633974483)
#printing rectangular form
print("the rectangular form - complex number:", end="")
print(w)