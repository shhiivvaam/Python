# for i in "myblog":
#     print(i , "?")

# for j in "myblog":
#     print(j , "y")

# for i in range (5):
#     print(i)

'''first 10 natural no.'''
# for i in range (1,11):
#     print(i)

'''first 10 even no.'''
# for i in range (2,20,2):
#     print(i)

'''first 10 odd no.'''
# for i in range (1,21,2):
#     print(i)

'''for 10 even in reverse'''
# for i in range (20,0,-2):
#     print (i)

'''table ,user defined'''
# n = int(input())
# for i in range (1,11):
#     table = n*i
#     print(table)

# # OR 

# num = int(input())
# for i in range (1,11):
#     print(num*i)

'''product of digits, user defined'''
# n = int(input())
# m = int(input())
# print(n*m)

# OR

# num = int(input())
# p = 1
# while (num):
#     r = num % 10
#     p = p * r
#     num = num // 10
# print("product : " , p)

# n = int(input("enter"))
# m = 1
# z = n*m
# while (n % m) :
#     print(" you have given" , n ,",this no. to ne multiplied by one_1")
# print(z)

# n = int(int(input("enter")))
# for m in range (1,11):
#     k = n * m
#     print(k)
#     w = 0
#     for q in range(n,n*m+1,n):
#         w += q
# print(w)

# a = int(input("enter"))
# b = 0
# for i in range (1,11):
#     c = a*i
#     b += c
#     print(c)
# print(b)

# """sum of digits accepted from the user"""
# num = int(input("enter any no."))
# s = 0
# while(num):
#     r = num % 10
#     s = s + r
#     num = num//10
#     print("sum of digits is : ",s)\

''' niche wala code galat hai'''

# a = int(input("enter the number : "))
# b = 0
# if a%3 == b:
#     print("this is a prime no.")
# else:
#     print("this is not a prime no.")

# a = int(input("enter the no. : "))
# b = a%2
# c = a%3
# if a == b and a == c:
#     print("no. is not a prime")
# else:
#     print("no. is prime")

# num=int(input("Enter any number"))
# f=0
# if num==1 or num==0:
#      f=1
# for i in range(2,num):
#      if num%i==0:
#           f=1
# if f==1:
#      print("Number is not prime")
# else:
#      print("Number is prime")

n = int(input("enter the no. of your choics: "))
a = 0
if n==0 or n==1:
     a = 1
for i in range (2,n):
     if n%i == 0:
          a = 1
if a==1:
     print("no is not prime : ",n)
else:
     print("no is prime : ",n)
print("thankyou")
