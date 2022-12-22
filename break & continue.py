students = ["ram" , "shyam" , "radha" , "kishn" , "radhika"]

for student in students:
    if student == "radha":
        break
    print(student)

# below code is not same, see the difference
for student in students:
    if student == "radha":
        break
    print(students)

for student in students:
    if student == "radha":
        continue
    print(student)