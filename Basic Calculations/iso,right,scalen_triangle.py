# '''Program to find whether a triangle is scalene, isosceles, right angled or invalid when the sides of the triangle are entered by the user.'''

print("Enter all the sides of the triangle")
h = (float(input('Enter the height of triangle : ')))
l = (float(input('Enter the length of the triangle : ')))
b = (float(input('Enter the base length of the triangle : ')))

if (b+h>l) or (h+l>b) or (l+b>h) :
    
    if (b**2+h**2==l**2) or (h**2+l**2==b**2) or (l**2+b**2==h**2):
        print("this is a right angled triangle")

    elif b==h!=l or h==l!=b or l==b!=h:
        print("this is a isosceles triangle")
    
    elif b!=h!=l:
        print("this is an scalene triangle")

    else :
        print("invalid inputs, try giving iput again with other values")

print("thankyou")


# if (h**2 != (l + b)**2) or (b**2 != (l + h)**2) or (l**2 != (h + b)**2):
#     print("enter valid input , values entered by you does'nt satisfies the properties of any triangle")

# d = (h * b)/2

# if (b != h) & (h != l) & (l != b) :
#     print(d)
#     print("according to the given input the , triangle is an scalene triangle")

# e = b*h/2
# f = (h**2 + b**2)**1/2

# print("thankyou")

# A=hbb/2 scalene

# A=bhb/2 isoscles

# c=(a^2+b^2)^1/2 right angled