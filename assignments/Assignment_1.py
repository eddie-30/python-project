# """
# Write a python script that takes input from a user and displays it to the 
# user in well formatted output. (use the concept of lists)
# Name age class gender telephone
# """

userDetails = []
userInput = input("Enter a name: ")
userDetails.append(userInput)
userInput = input("Enter age: ")
userDetails.append(userInput)
userInput = input("Ener class: ")
userDetails.append(userInput)
userInput = input("Enter gender: ")
userDetails.append(userInput)
userInput = input("Enter telephone: ")
userDetails.append(userInput)

print(f"Your name is {userDetails[0]}, Your age is {userDetails[1]}, Your class is {userDetails[2]}, Your gender is {userDetails[3]}, Your telephone is {userDetails[4]}")

print(userInput)
print(userDetails)

