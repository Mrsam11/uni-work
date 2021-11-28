# def diamond(a):
#     for i in range(a):
#         print(' '*(a-i-1)+'*'*(i+1))
#     for j in range(a-1,0,-1):
#         print(' '*(a-j)+'*'*(j))
# diamond(4)
def pyramid(rows):
    for i  in range(rows):
        print(" "*(rows-i-1)+"*"*(2*i+1))
    for j in range(rows-1,0,-1):
        print(" "*(rows-j)+"*"*(2*j-1))

rows = int(input("Enter number of rows : "))
pyramid(rows)