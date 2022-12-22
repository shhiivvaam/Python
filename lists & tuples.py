# lists , tuples & slicing

''' lists '''

'''
#sort : sorts the list
#reverse : reverses the list
#append : adds one(1) element ata the end of the list
#insert : adds element at the given index
#pop : delete the element from the list when given the elements index
#remove : removes that particular element from the list
'''

a = ["hehe","1","charles23"]
print(a)
print(a[:3])
print([-2])

b = [1,2,3,4,5,6,7,8,9]
print(b) 
b.sort()
print(b)
b.reverse()
print(b)
b.append(10)
print(b)
b.insert(10,11)
print(b) 
b.pop(2)
print(b)
b.remove(3)
print(b)

''' tuples '''

'''
# a = () : empty tuple
# a = (1,) : tuple with only one element
# a = (1,2,3,4) : tuple with more than one element'''

'''
tuples are immutable : once defined ,cannot be changed further
'''

t = (1,2,3,4,1,2,3,4,1,2,3,4)
print(t)
r = (1,)
print(r) 
print(t.count(1))
print(t.index(3))

'''practise problems'''

#1
a = input("enter the fruit name here")
b = input("enter the fruit name here")
c = input("enter the fruit name here")
d = input("enter the fruit name here")
e = input("enter the fruit name here")
f = input("enter the fruit name here")
g = input("enter the fruit name here")
list = [a,b,c,d,e,f,g]
print(list)

#2
a = int(input("enter the marks here : "))
b = int(input("enter the marks here : "))
c = int(input("enter the marks here : "))
d = int(input("enter the marks here : "))
e = int(input("enter the marks here : "))
f = int(input("enter the marks here : "))
g = int(input("enter the marks here : "))
list = [a,b,c,d,e,f,g]
list.sort()
print(list)

#3
'''a = (1,2,3,4,5,6,)
a[2] = 4'''

#4
a = [1,2,3,4]
print(a[0]+a[1]+a[2]+a[3])

a = [1,2,3,4]
print(sum(a))

#5
a = (7,0,8,0,0,9)
b = a.count(0)
print(b)
