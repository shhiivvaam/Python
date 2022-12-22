'''Conditional expressions'''

#if
#elif
#else

'''(if) will execute first then if (if) will get_TRUE then elif and else will not execute'''
'''and if (if) gets_FALSE then elif will execute and then if (elif) gets_TRUE then (else) will not execute '''
'''if elif gets_FALSE then else will execute'''

'''if all the conditional statements of (elif) will gets_FALSE then (else) will execute'''

# if , elif , else statements

a = int(input("Enter the choice of any digit number b/w 1 to 10, you want to check : \n"))

if (a>9):
    print("the given value is greater than 9")
elif (a>8):
    print("the number is greater then 8")
elif (a>7):
    print("the number is greater then 7")
elif (a>6):
    print("the number is greater then 6")
elif (a>5):
    print("the number is greater then 5")
elif (a>4):
    print("the number is greater then 4")
elif (a>3):
    print("the number is greater then 3")
elif (a>2):
    print("the number is greater then 2")
else :
    print("the number is greater than 1 or 0")

print("Thankyou")

b = int(input("enter your age : "))

if b>18 :
    print("yes you are above 18")
else :
    print("no you are not above 18")

print("Thankyou")

'''practise problems'''

#1
a = int(input("enter the number : "))
b = int(input("enter the number : "))
c = int(input("enter the number : "))
d = int(input("enter the number : "))

if a>d :
    q1 = a
else :
    q1 = d

if b>c :
    q2 = b
else :
    q2 = c

if(q1>q2):
    print(str(q1) + " is greatest")
else:
    print(str(q2) + " is greatest")

print("thanyou")