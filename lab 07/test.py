# def favorite_book(title):
#     print('One of My Favorite book is', title.title())
# 
# favorite_book('The easyest way to learn python')
# def max(a,b,c):
#     if i > j and i > k:
#         return i
#     if j > k and j>i:
#         return j
#     else:
#         return k
# 
# i = 10
# j =21
# k = 2
# z=max(i,j,k)
# print (z)
# def max2(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# def max3(x,y,z):
#     return max2(x, max2(y,z))
# print(max3(7,4,1))
# def describe_city(city,country ='Pakistan'):
#     print(city , 'is in' , country)
# describe_city('Karachi')
# describe_city('Lahore')
# describe_city('dehli','india')
# x = 20
# y = 12
# import math
# print(math.gcd(x,y))
def gcd(a,b):    #Euclid's Method
    if b==0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(48,64))