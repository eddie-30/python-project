#For loop in python
# range(start,stop,step)
for numbers in range(1,20):
    print(numbers)

# For intervals
for numbers in range(1,20,5):
    print(numbers)

# For revesrse
for numbers in range(20,1,-1):
    print(numbers)

# still works refering to 'start' 0-20
for numbers in range(21):
    print(numbers)

# Printing a single Character individually with loop
name="Joe"
print(name[2])
# -----------------------
# Printing all Characters individually with loop
for numbers in range(3):
    print(name[numbers])
# -----------------------
# Another Method
for x in name:
    print(x)

# Print from list with loops
student=["Joe","Peneil","Nessa","Abena"]
for x in student:
    print(student)
    print(student[1])
    print(student[1][1])


for times in range(1,13):
    print (f"2*{times} = {2*times}")

# to take a single input with loops
student=[]
name= input("Enter Student Name: ")
student.append(name)
for x in student:
    print(student)

# to take mutiple inputs with loops 
for number in range(5):
    name= input("Enter Student Name: ")
    student.append(name)
print(student)
