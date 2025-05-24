
#Task 1: Perform Basic Mathematical Operations

num1= float(input("Enter firts number: "))
num2= float(input("Enter second number: "))

# Perform addition, substraction and multiplication

addition = num1 + num2
substraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
     division = "FUCK YO, this CAN NOT divide by zero"



print("addition: ", addition)
print("substraction: ", substraction)
print("multiplication: ", multiplication)
print("division: ", division)




#Task 2: Create a Personalized Greeting

First_name= input("Enter_First_name: ")
Last_name= input("Enter_last_name: ")

full_name = First_name +" "+ Last_name



print("Hello, " + (full_name) + " Welcome to the PYTHON programe.")