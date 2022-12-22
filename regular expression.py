import re

st = "Python is a best language"
out = re.search("Python | python" , st)

print(out)
if out :
    print("match found")
else :
    print("not found")


out = " pyhton " in st

'''niche email k lia hai code'''

# import re

# st = "my email id is amirlhan1092@gmail.com amd my friend id is mandeep@gmail.com dfdsfdscsdcd"

# st = "the python is the best language"
# out = re.search("python .*  best" , st)  
# print(out.groups())

# st = "the python is ge The best language with online"
# out = re.search 



'''niche wala sahi hai bass re defined nhi hai, quki koi value given nhi hai_ re ka tu sir se puch'''

# st = '''my email id is amirlhan1092@gmail.com amd
# my friend id is mandeep@gmail.com dfdsfdscsdcd'''

# out = re.findall('[a-z0-9_]+[\.][a-z0-9]+',st)

# print(out)


# '''niche waala email k lia hai, try krio isse'''
# import re

# email = input("enter the email : ")

# out = re.search(' '. email)

# if out :
#     print("email id is valid")
# else :
#     print("email id is not valid")