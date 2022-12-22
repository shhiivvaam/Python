'''find all the words starting with non vowel and end with a vowel (using regex)'''


# import re

# st = input("enter the word ")

# pt = '^[^aeiou].*[aeiou]$'

# if re.search(pt, st):
#     print(st)

'''finding the matching word using findall(find)'''

import re

st = "python rate base mate gla"

pt = r'\b[^aeiou]\w+[aeiou]\b'

out = re.findall(pt,st)

print(out)

