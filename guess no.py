# game : guess the number.


import random as r
r.seed(10)
num = r.randint(1,100)
a = True
c = 1
while c <= 10 :
    y = int(input("Guess the Number"))
    if y>num:
        print("Too large")
    elif y<num:
        print("Too Small")
    else:
        print("you won with ",c , "tries.")
        break
    c += 1
else:
    print("you lost")