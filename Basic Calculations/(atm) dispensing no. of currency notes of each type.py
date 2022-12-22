n = int(input("enter the no. of notes you want to dispense : "))

n = n - 100

a = n // 2000
n = n - (a*2000)

b = n // 500
n = n - (b*500)

c = n // 200
n = n - (c*200)

d = (n // 100)+1

print(a)
print(b)
print(c)
print(d)
print(n)

ssbig si