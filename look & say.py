n=int(input("no. of lines you want : "))
value = 1
print(value)
while n > 1:
    b = " "
    while value > 0:
        c = value % 10
        count = 1
        value //= 10
        while value > 0 and value % 10 == c:
            count += 1
            value //= 10
        b = str(count) + str(c) + b
    print(b)
    value = int(b)
    n -= 1