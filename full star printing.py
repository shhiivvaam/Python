# star printing from various ways and sides

a = int(input('enter the value'))
for i in range (a):
    for j in range (a):
        print('# ',end = '')
    print()

b = int(input("enter the value"))
for i in range (b):
    for j in range (i+1):
        print("*",end= " ")
    print()

c = int(input("enter the value"))
for i in range (c):
    for j in range (i+1,c):
        print("  ",end="")
    for j in range (i+1):
        print(" *",end="")
    print()

''' 1
   2 3
  4 5 6
7 8 9 1 0'''
# printng numbers in star format done above

n = int(input("enter the value"))

k = 1
for i in range(n):
    for j in range(i+1):
        print(k,end=' ')
        k+=1
    print()

k = 1
for i in range(n):
    for j in range(n-1,i,-1):
        print(" ",end=' ')
    for j in range(i+1):
        print(k,end='  ')
        k+=1
    print()

''''niche wala har type k star pattern print kr sakta hai , bass space ka gap change krke'''
# niche wala toop code hai , sare typr k standing star pattern print kr sakta hai

h = int(input())
for i in range(1, h+1):
    print(' '*(h-i)+'*'*(2*i-1))  


'''ye wala best code hai standing star pattern print k lia'''
a = int(input("enter : "))
for i in range (1 , a+1):
    print(" "*(a-i)+"$"*(2*i-1))

