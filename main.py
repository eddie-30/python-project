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

# Calcutaions PEMDAS (Parenthesis, exponet, multiplication, division Subtaction)
# Logic (Not, And, or)
# Operators (and, 
#            or, 
#            < {Greater than}, 
#            > {Less than}, 
#            >= {Greater than or equal to}, 
#            <= {Less than or equal to},
#            == {Equal to},
#            != {not equal to}
#            not     )


a = 6 
print (a == 5)

gender= "female"
age = 12
print (gender=="Female" or age == 12)
# output = True ( or means either 1 answer is True)
print (gender=="Female" and age == 12)
#output = false ( and means both answers are false)

gender= "female"
age = 9
print (gender=="Female" or age != 12)
#output = true ( means age is not equal to 12)
print (gender=="Female" or age > 12)
#output = false (means age is not greater than 12 )
print (gender=="Female" or age >= 12)
#output = false (means age is not greater than or equal to 12 )


# Conditional Statements
age = input("Enter your age: ")
if age < "18":
    print ("You are not allowed to drive")

if age == "18" and age <= "79":
    print ("You can drive")
else : print ("You are not allowed to drive")

if age == "18" and age <= "79":
    print ("You can drive")


