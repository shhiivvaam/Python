marks = [10,20,30]

marks.append(40)
marks.insert(4,50)

for score in marks:
    print(score)

print(10 in marks)
print(15 in marks)

print(len(marks))

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

marks.clear()
print(marks)