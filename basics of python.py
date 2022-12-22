# started learning code
'''let's get started'''

'''python automatically detects wheather the number
    given by the operator is string(str) ,float(float)
    or integer(int)'''


#Assignment Operators
'''all -(subtract) , +(addition) , 
    *(multiplication) , %(remainder) ; signs are known
    as assignment operators'''

a  = 5
a -= 5
a *= 5
a %= 5
print(a)

#Comparison Operators
'''all <(greater than) , >(smaller than) ,
    ==(equal to equal to) , <=(greater tham equal to) ,
    >=(smaller than equal to)'''

b = (1<=2)
print(b)

#Logical Operators
'''AND : both true _ TRUE , in any other case _ FALSE
   OR  : any true _ TRUE  , in any other case _ FALSE
   NOT : makes the opposite , i.e: if true then FALSE
                                   if flase then TRUE'''

c1 = True
c2 = False
print(c1)
print(c1 and c2)
print(c1 or c2)
print(not c2)
print(c2)

# Problem Solving

#1
a = 30
b = 15
print("this is your required remainder : ", a % b)

#2
a = input("enter the 1st number you want : ")
b = input("enter the 2nd number you want : ")
a = int(a)
b = int(b)
c = (a + b) / 2
print("this is the average of the two numbers given by you : ", c)

#3
a = int(input("enter the number you want"))
b = a*a
print("this is the square of your given number : ",b)

#4
a = int(input("enter the number you want"))
b = a**2
print("this is the square of your given number : ",b)

# Membership Operators

'''if , else , elif , while'''