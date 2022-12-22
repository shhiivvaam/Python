# write a program to generate the 6 digit otp.


import random as rd

width = 6

num = rd.random()
otp = str(num)[-width:]
print(otp)