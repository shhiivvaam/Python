# Program to find the Simple Interest and the total amount when the Principal, Rate of Interest and Time are entered by the user.

p = (int(input("enter the [P] principal amount : ")))
r = (float(input("enter the [R] rate amount : ")))
t = (int(input("enter the [T] interest time duration : ")))

d = (p*(1+(r/100))**t)-p

print("total amount with simple intrest is : ",d)


# a = p(1+rt) '''simple interest'''
# F = P(1 + i)^N '''total amout formula'''
