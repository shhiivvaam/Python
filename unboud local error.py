def add():
    global a
    print(a) #global reference
    a = 1 #local variable asssignment
a = 10
add()