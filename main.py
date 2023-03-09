# Creating Variables and |Printing
name= "Edinam Ahianyo"
phone_number= 507597909
age= 18
print(name)
print(phone_number)
print(age)
names_of_students= ["Kwadjo","Ama","Yaw","Joel","Edinam"]
Second_student= names_of_students[1]
print(Second_student)
names_of_students.append ("Micheal")
print(names_of_students)
# Creating a list
third_student = names_of_students[2]
print(third_student)
names_of_students.pop(2)
list= ["A","B","C"]
#dictionary
my_details= {"Name":"Edinam", "Nicki":"Edibles", "Habibi":"Joel"}
joels_info= {
    "name":"Joel",
    "age": 18,
    "hobbies": {"outdoor": ["Roaming", "Ampe"], 
    "indoor":["ludo","Uno"]} 
    }

hobbies= joels_info["hobbies"]
print(f"my hoobies are {hobbies}")

Outdoor= hobbies["outdoor"]
print(f"Outdoor hoobies are {Outdoor})")

second_outdoor_hobby = Outdoor[1]

print(second_outdoor_hobby)

#Adding and Removing Names And Grades to A Dictionary
student_grade ={}
student_grade["Mike"]="A"
print(student_grade)
student_grade["Selasi"]="B"
print(student_grade)
student_grade["Eugene"]="C"
print(student_grade)
student_grade.pop ("Selasi")
print(student_grade)

# Input in python
age= input("What is your age?\n")
# print(age)
print(f"Your age is {age}")