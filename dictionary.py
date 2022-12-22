from typing import Collection


dict = {"fast" : "In a quick manner" , "Shivam" : "A coder"}
print(dict)

mydict = {
    "fast" : "In a manner" ,
    "Shivam" : "a coder" ,
    "marks" : [1,2,3] , 
    "anotherdict" : {"shivam" : "player"}
}

print(mydict["fast"])
print(mydict["Shivam"])
print(mydict["marks"])
print(mydict["anotherdict"]["shivam"])

print(type(mydict.values()))
print(type(mydict.keys()))
print(type(mydict))

print(list(mydict))

print(list(mydict.values()))
print(list(mydict.keys()))
print(tuple(mydict.keys()))

'''practise problems'''

#1
mydict = {
    "pankha" : "fan" , 
    "dabba" : "box" , 
    "vastu" : "item" 
}
print("options are" , mydict.keys())
a = input("enter the hindi word\n")
print("the meaning of your word is : ", mydict[a])


#print("the meaning of your word is : ", mydict.get(a))
'''above line will not give an error if the word/ key is not present is the dictionary'''

#2
a1 = input("enter the number 1 ")
a2 = input("enter the number 2 ")
a3 = input("enter the number 3 ")
a4 = input("enter the number 4 ")
a5 = input("enter the number 5 ")
a6 = input("enter the number 6 ")
a7 = input("enter the number 7 ")
a8 = input("enter the number 8 ")
a = {a1 , a2 , a3 , a4 , a5 , a6 , a7 , a8}
print(a)

#6
favlang = {}
a = input("enter your favourute language shubham\n")
b = input("enter your favourute language ankit\n")
c = input("enter your favourute language surya\n")
d = input("enter your favourute language shivam\n")
favlang["shubham"] = a
favlang["ankit"] = b
favlang["surya"] = c
favlang["shivam"] = d
print(favlang)