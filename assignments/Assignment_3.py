bill = 0 

print("Welcome to ESA Pizza Delivery")

size = input("Which size do you want? L, M, S: ")
add_pepperoni = input ("Do you want to add pepperroni? Y or N: ")
extra_chesse = input ("Do you want chesse? Y or N:  ")

if size =="L":
    bill += 100
elif size == "M": 
    bill += 85
else:
    bill += 50 
if add_pepperoni == "Y":
    bill += 10
if extra_chesse == "Y":
    bill += 5
print (f"The total  bill is {bill}")
