n = int(input("enter the no. for you pattern to be printed soon"))
for i in range (1,n+1):
    for i in range(i):
        print("*" , end =" ")
        for i in range (i):
            print('*',end = ' ')
print(n)